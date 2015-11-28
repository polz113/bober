from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from forms import OverviewForm, SchoolCodesCreateForm
from bober_simple_competition.views import AccessCodeRequiredMixin, SmartCompetitionAdminCodeRequiredMixin
from bober_simple_competition.views import safe_media_redirect, user_files, _user_file_path
from bober_simple_competition.models import Attempt, Profile, GradedAnswer, AttemptConfirmation
from bober_paper_submissions.models import JuniorDefaultYear
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from models import *
from forms import *
from collections import OrderedDict, defaultdict
from braces.views import LoginRequiredMixin
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
import datetime
import os
from award_gen import generate_award_pdf
# Create your views here.

AWARD_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'award_templates')

class TeacherOverview(SmartCompetitionAdminCodeRequiredMixin, 
        TemplateView):
    template_name="bober_si/teacher_overview.html"

    def dispatch(self, *args, **kwargs):
        competition = SchoolCompetition.get_cached_by_slug(slug=kwargs['slug'])
        access_code = self.request.session['access_code']
        self.competition = competition
        return super(TeacherOverview, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TeacherOverview, self).get_context_data(**kwargs)
        profile = self.request.user.profile
        context['profile'] = profile 
        context['competition'] = self.competition
        school = None
        schools = dict()
        attempts = dict()
        code_pairs = []
        school_categories = set()
        for c in profile.schoolteachercode_set.filter(
                    code__codegenerator = self.competition.competitor_code_generator
                ).order_by(
                    'school', 'code'
                ).prefetch_related(
                    'school', 'code',
                ):
            if c.school != school:
                schools[c.school] = []
                attempts[c.school] = []
            school = c.school
            school_categories.add(school.category)
            code = c.code.value
            sep = self.competition.competitor_code_generator.format.separator
            split_code = code.split(sep)
            cqs_slug = split_code[0]
            cqs = CompetitionQuestionSet.get_by_slug(cqs_slug)
            schools[school].append((cqs, sep.join(split_code[1:])))
            a_list = []
            all_attempts = Attempt.objects.filter(
                access_code = code).select_related(
                    'competitor',
                    'competitionquestionset',
                    'competitionquestionset__questionset').prefetch_related(
                    'gradedanswer_set',
                    'competitionquestionset__questionset__questions',
                )
            confirmed_attempts = all_attempts.filter(
                confirmed_by__id=profile.id,    
            )
            unconfirmed_attempts = all_attempts.exclude(
                confirmed_by__id=profile.id,
            )
            for a in confirmed_attempts.all():
                a_list.append((a, 'confirmed'))
            for a in unconfirmed_attempts.all():
                a_list.append((a, 'unconfirmed'))
            attempts[school].append((cqs, a_list))
        show_paper_results = JuniorDefaultYear.objects.filter(
            competition = self.competition,
            school_category__in = school_categories,
            ).exists()
        context['show_paper_results'] = show_paper_results
        context['show_codes'] = self.competition.end >= timezone.now()
        context['schools'] = schools
        context['attempts'] = attempts
        context['junior_mentorships'] = profile.juniormentorship_set.filter(
            competition = self.competition).prefetch_related('junioryear_set', 
                'junioryear_set__juniorattempt_set', 'junioryear_set__juniorattempt_set__competitor')
        # print attempts
        return context

class SchoolCodesCreate(SmartCompetitionAdminCodeRequiredMixin, FormView):
    template_name="bober_si/school_codes_create.html"
    form_class = SchoolCodesCreateForm
    def dispatch(self, *args, **kwargs):
        self.competition = SchoolCompetition.objects.get(slug=kwargs['slug'])
        self.next_url = self.request.GET.get('next_url', None)
        self.access_code = self.request.session['access_code']
        codegen = self.competition.administrator_code_generator
        if not codegen.code_matches(self.access_code, 
                {'admin_privileges': ['create_competitor_codes']}):
            raise PermissionDenied
        return super(SchoolCodesCreate, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(SchoolCodesCreate, self).get_context_data(**kwargs)
        context['next_url'] = self.next_url
        return context
    def form_valid(self, form):
        school = form.cleaned_data['school']
        self.competition.school_codes_create(
            school, self.request.user.profile, 
            self.request.session['access_code']) 
        return super(SchoolCodesCreate, self).form_valid(form)
    def get_success_url(self):
        if self.next_url is None:
            return reverse('index')
        return self.next_url

class TeacherCodeRegistrationPasswordReset(FormView):
    form_class = TeacherCodeRegistrationPasswordResetForm
    template_name="bober_si/teacher_registration_password_reset.html"
    def dispatch(self, *args, **kwargs):
        self.competition = Competition.objects.get(slug=kwargs['slug'])
        return super(TeacherCodeRegistrationPasswordReset, self).dispatch(*args, **kwargs)
    def get(self, *args, **kwargs):
        try:
            code = self.competition.administrator_code_generator.codes.get(value=self.request.GET['hidden_code'])
        except:
            response = render(self.request, 'bober_si/no_hidden_code.html')
            response.status_code = 403
            return response
        return super(TeacherCodeRegistrationPasswordReset, self).get(*args, **kwargs)
    def get_initial(self):
        initial = super( TeacherCodeRegistrationPasswordReset, self).get_initial()
        initial['hidden_code'] = self.request.GET.get('hidden_code', '')
        return initial
    def form_valid(self, form):
        retval = super( TeacherCodeRegistrationPasswordReset, self).form_valid(form)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            code = self.competition.administrator_code_generator.codes.get(value=form.cleaned_data['hidden_code'])
        except:
            response = render(self.request, 'bober_si/no_hidden_code.html')
            response.status_code = 403
            return response
        try:
            user = User.objects.get(email = email)
        except:
            user = User(username=email, email=email)
        user.set_password(password)
        user.save()
        user.profile.managed_profiles.add(user.profile)
        user.profile.received_codes.add(code)
        u = authenticate(username = user.username, password=password)
        login(self.request, u)
        return retval
    def get_success_url(self):
        return reverse('teacher_overview', kwargs={"slug":self.competition.slug})

class ProfilesBySchoolCategory(SmartCompetitionAdminCodeRequiredMixin, TemplateView):
    template_name = 'bober_si/profiles_by_schooltype.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProfilesBySchoolCategory, self).get_context_data(*args, **kwargs)
        categories = dict()
        for category in SCHOOL_CATEGORIES:
            profiles = Profile.objects.filter(
                schoolteachercode__school__category=category[0], 
                schoolteachercode__code__codegenerator = self.competition.competitor_code_generator,
            ).distinct()
            if profiles.count() > 0:
                categories[category] = profiles
        context['categories'] = categories
        return context
    def dispatch(self, *args, **kwargs):
        self.competition = SchoolCompetition.objects.get(slug = kwargs.pop('slug'))
        if not self.competition.administrator_code_generator.code_matches(self.access_code, 
                {'admin_privileges': ['view_all_competitor_codes']}):
            raise PermissionDenied
        return super(ProfilesBySchoolCategory, self).dispatch(*args, **kwargs)


class CompetitionXlsResults(SmartCompetitionAdminCodeRequiredMixin, TemplateView):
    template_name = 'bober_si/competition_results.xls'

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.excel_results(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" )
    
    def excel_results(self):
        def profiles_str(p_list):
            return u", ".join([
                u"{} <{}>".format(
                    i.user.username, i.user.email
                ) for i in p_list])
        wb = Workbook()
        ws = wb.get_active_sheet()
        for cqs in self.competitionquestionsets.all():
            # t0 = datetime.datetime.now()
            profiles_by_code = defaultdict(list)
            schools_by_code = defaultdict(list)
            schools_by_teacher = defaultdict(list)
            for code in self.competition.competitor_code_generator.codes.filter(
                    value__startswith = cqs.slug_str()
                ):
                for p in code.creator_set.all().select_related('user'):
                    profiles_by_code[code.value].append(p)
                for sct in code.schoolteachercode_set.all():
                    schools_by_code[code.value].append(sct.school)
                    schools_by_teacher[sct.teacher_id].append(sct.school)
            
            ws.title = cqs.name
            questions = cqs.questionset.questions.order_by('id')
            keys = [
                'Attempt ID',
                'Start',
                'Finish',
                'Code',
                'Competition',
                'Possible schools',
                'Confirmed schools',
                'Confirmed by',
                'No. of confirmations',
                'Possible mentors',
                'Group',
                'First name',
                'Last name',
            ]
            question_none_scores = dict()
            for q in questions:
                keys.append(str(q))
                question_none_scores[q.id] = q.none_score
            ws.append(keys)
            #all_answers = dict()
            #for g_ans in GradedAnswer.objects.filter(
            #            attempt__competitionquestionset = cqs
            #        )
            #    all_answers[(g_ans.attempt_id, g_ans.question_id)] = g_ans
            # print "    got data in ", datetime.datetime.now() - t0
            gradedanswers = dict()
            for attempt_id, question_id, score in GradedAnswer.objects.filter(
                    attempt__competitionquestionset__id = cqs.id
                ).distinct().values_list(
                    'attempt_id', 'question_id', 'score'):
                gradedanswers[(attempt_id, question_id)] = score
            confirmations = defaultdict(list)
            for by_id, attempt_id, username, email in AttemptConfirmation.objects.filter(
                    attempt__competitionquestionset__id = cqs.id
                ).distinct().values_list(
                    'by_id',
                    'attempt_id',
                    'by__user__username', 'by__user__email'):
                confirmations[attempt_id].append((
                    by_id,
                    u"{} <{}>".format(username, email)
                ))
            attempts = cqs.attempt_set.all()
            for (
                    attempt_id,
                    attempt_start,
                    attempt_finish,
                    access_code,
                    first_name,
                    last_name,
                ) in attempts.values_list(
                    'id',
                    'start',
                    'finish',
                    'access_code',
                    'competitor__first_name',
                    'competitor__last_name',
                ).distinct():
                # print "  attempt:", attempt.id
                mentors = profiles_by_code[access_code]
                schools = schools_by_code[access_code]
                # confirmed_by = attempt.confirmed_by.all()
                confirmed_schools = set()
                #if competitor is None:
                #    first_name = 'A. Nonny'
                #    last_name = 'Moose Guest'
                #else:
                #    first_name = competitor.first_name
                #    last_name = competitor.last_name
                confirmed_by = confirmations[attempt_id]
                for p in confirmed_by:
                    for s in schools_by_teacher[p[0]]:
                        confirmed_schools.add(s)
                confirmed_by_schools = set(schools).intersection(
                    confirmed_schools)
                #print "    ", confirmed_by
                l1 = [
                    attempt_id,
                    attempt_start,
                    attempt_finish, 
                    access_code,
                    self.competition.slug,
                    u", ".join([i.name for i in schools]),
                    u", ".join([i.name for i in confirmed_by_schools]),
                    ", ".join([i[1] for i in confirmed_by]),
                    len(confirmed_by),
                    profiles_str(mentors),
                    cqs.name,
                    first_name,
                    last_name,
                ]
                for q in questions:
                    l1.append(gradedanswers.get((attempt_id, q.id), 
                        question_none_scores[q.id]))
                #print "    ", l1
                ws.append(l1)
            ws = wb.create_sheet()
        return save_virtual_workbook(wb)

    def dispatch(self, *args, **kwargs):
        self.competition = SchoolCompetition.get_cached_by_slug(slug = kwargs.pop('slug'))
        if not self.competition.administrator_code_generator.code_matches(
                self.request.session['access_code'], 
                {'admin_privileges': ['view_all_competitor_codes']}):
            raise PermissionDenied
        self.competitionquestionsets = CompetitionQuestionSet.objects.filter(
            competition = self.competition)
        cqs_id = kwargs.pop('cqs_id', None)
        if cqs_id is not None:
            self.competitionquestionsets = self.competitionquestionsets.filter(id=cqs_id)
        return super(CompetitionXlsResults, self).dispatch(*args, **kwargs)

@login_required
def award_pdf(request, slug, school_id, cqs_name):
    profile = request.user.profile
    cert_dir = os.path.join(_user_file_path(profile, school_id))
    cert_fname = cqs_name + '.pdf'
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
    try:
        # print "f:", os.path.join(settings.MEDIA_ROOT, cert_path)
        assert os.path.isfile(cert_full_fname)
    except:
        try:
            cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
            os.makedirs(cert_full_dir)
        except Exception, e:
            pass
            print e
        # regenerate award. Ignore the template
        template_file = os.path.join(AWARD_TEMPLATE_DIR, 'all_si.svg')
            #print "generating..."
        data = list()
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        for stc in profile.schoolteachercode_set.filter(
                    code__codegenerator = competition.competitor_code_generator,
                    competition_questionset__name = cqs_name,
                    school__id = school_id
                ).order_by(
                    'code'
                ).prefetch_related(
                    'code'):
            school = stc.school
            code = stc.code.value
            cqs = stc.competition_questionset
            #print "    ", school, cqs
            #CompetitionQuestionSet.objects.get(competition=competition,
            #    name = cqs_name)
            confirmed_attempts = Attempt.objects.filter(
                    access_code = code,
                    competitionquestionset = cqs,
                    confirmed_by__id=profile.id,
                ).select_related(
                    'competitor',
                ).prefetch_related(
                    'attemptaward_set',
                )
            for attempt in confirmed_attempts:
                for award in attempt.attemptaward_set.all().select_related('award'):
                    data.append(
                        {
                            'name': u" ".join((attempt.competitor.first_name, attempt.competitor.last_name)),
                            'school': school.name,
                            'group': cqs.name,
                            'serial': award.serial,
                            'template': award.award.template,
                        }
                    )
        #    print data
        #print os.path.join(cert_full_dir, cert_fname)
        generate_award_pdf(cert_full_fname,
            data, template_file)
        
    #return None
    return safe_media_redirect(cert_path)

@login_required
def invalidate_award(request, slug, profile_id, school_id, competition_questionset_id):
    
    pass
