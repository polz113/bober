#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from forms import OverviewForm, SchoolCodesCreateForm
from bober_simple_competition.views import AccessCodeRequiredMixin, SmartCompetitionAdminCodeRequiredMixin
from bober_simple_competition.views import safe_media_redirect, _profile_file_path, JsonResponse
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
import cairosvg

# Create your views here.

class TeacherOverview(SmartCompetitionAdminCodeRequiredMixin, 
        TemplateView):
    template_name="bober_si/teacher_overview.html"

    def dispatch(self, *args, **kwargs):
        try:
            competition = SchoolCompetition.get_cached_by_slug(slug=kwargs['slug'])
        except:
            raise Http404
        access_code = self.request.session['access_code']
        self.competition = competition
        return super(TeacherOverview, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TeacherOverview, self).get_context_data(**kwargs)
        profile = self.request.profile
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
                'junioryear_set__attempts', 'junioryear_set__attempts__competitor')
                # 'junioryear_set__juniorattempt_set', 'junioryear_set__juniorattempt_set__competitor')
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
            school, self.request.profile, 
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
                'Awards',
                'Revoked awards',
                'Score'
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
            awards = defaultdict(list)
            revoked_awards = defaultdict(list)
            for attempt_id, revoked_by, award_name in AttemptAward.objects.filter(
                        attempt__competitionquestionset__id = cqs.id
                    ).distinct().values_list('attempt_id', 
                        'revoked_by',
                        'award__name'):
                if revoked_by is not None:
                    revoked_awards[attempt_id].append(award_name)
                else:
                    awards[attempt_id].append(award_name)
            attempts = cqs.attempt_set.all()
            for (
                    attempt_id,
                    attempt_start,
                    attempt_finish,
                    access_code,
                    first_name,
                    last_name,
                    attempt_score,
                ) in attempts.values_list(
                    'id',
                    'start',
                    'finish',
                    'access_code',
                    'competitor__first_name',
                    'competitor__last_name',
                    'score',
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
                    u", ".join(awards[attempt_id]),
                    u", ".join(revoked_awards[attempt_id]),
                    attempt_score,
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
def mentor_certificate_pdf(request, username):
    
    def _compose_text(name, nschool, awards):
        class Plural:
            def __init__(self, *forms):
                self.forms = forms

            def __getitem__(self, n):
                n %= 100
                if n == 4: n = 3
                elif n >= 5: n = 4
                n -= 1
                if n >= len(self.forms): n = 2
                return self.forms[n]

        class Numbers:
            def __init__(self, *forms):
                self.forms = forms

            def __getitem__(self, n):
                return self.forms[n - 1] if n - 1 < len(self.forms) else str(n)

        p_tekmovalcu = Plural(u"tekmovalcu", u"tekmovalcema", u"tekmovalcem")
        p_tekmovalec = Plural(u"tekmovalec", u"tekmovalca", u"tekmovalci", u"tekmovalcev")
        p_je = Plural(u"je", u"sta", u"so", u"je")
        p_se_je = Plural(u"se je", u"sta se", u"so se", u"se je")
        p_osvojil = Plural(u"osvojil", u"osvojila", u"osvojili", u"osvojilo")
        p_uvrstil = Plural(u"uvrstil", u"uvrstila", u"uvrstili", u"uvrstilo")
        n_nom = Numbers(u"En", u"Dva", u"Trije", u"Štirje", u"Pet", u"Šest", u"Sedem", u"Osem", u"Devet")
        n_dativ = Numbers(u"enemu", u"dvema", u"trem", u"štirim", u"petim", u"šestim", u"sedmim", u"osmim", u"devetim")

        res = u"{} je bil(a) mentor(ica)\n" \
              u"{} {} na šolskem nivoju\n" \
              u"mednarodnega tekmovanja Bober, 9. - 13. novembra 2015.\n \n".\
                  format(name, n_dativ[nschool], p_tekmovalcu[nschool])
        awards.pop(u"priznanje", 0)
        n = awards.pop(u"napreduje", 0)
        if n:
            res += u"{} {} {} {} na\ndržavno tekmovanje 16. januarja 2016.\n\n". \
                   format(n_nom[n], p_tekmovalec[n], p_se_je[n], p_uvrstil[n])
        for a in (u"bronasto", u"srebrno", u"zlato"):
            n = awards.pop(a, 0)
            if n:
                res += u"{} {} {} na {} nivoju {} {} priznanje.\n".format(
                       n_nom[n], p_tekmovalec[n], p_je[n],
                       [u"šolskem", u"državnem"][a != u"bronasto"], p_osvojil[n], a)
        if awards:
            res += u"\nUvrstitve na državnem tekmovanju:\n" + \
                   u",\n".join(u"- {} {} {} {} na {} mesto".format(
                       n_nom[n], p_tekmovalec[n], p_se_je[n], p_uvrstil[n], nm)
                      for n, nm in (
                           (awards[a], nm)
                           for a, nm in ((u"prva", u"prvo"), (u"druga", u"drugo"), (u"tretja", u"tretje"))
                           if awards.get(a, 0))) + \
                   u".\n"
        return res

    def _create_mentor_certificate(user, sc_slug, st_slug):
        icodes = user.created_codes.all()
        nschool = nstate = 0
        awards = defaultdict(int)
        for icode in icodes:
            for attempt in Attempt.objects.filter(access_code=icode):
                if attempt.competition.slug == sc_slug:
                    if list(attempt.confirmed_by.all()) != [user]:
                        continue
                    nschool += 1
                elif attempt.competition.slug == st_slug:
                    nstate += 1
                else:
                    continue
                for award in set(award.award.name for award in attempt.attemptaward_set.all()):
                    awards[award] += 1
        name = (user.first_name.strip() + u" " + user.last_name.strip()).title()
        text = _compose_text(name, nschool, awards)
        text = "\n".join(map(u'<tspan x="0" dy="1.2em">{}</tspan>'.format, text.splitlines()))
        cert_dir = os.path.join(settings.MEDIA_ROOT, _profile_file_path(user, ""))
        try:
            os.mkdir(cert_dir)
        except:
            pass
        template_file = os.path.join(AWARD_TEMPLATE_DIR, 'certificate.svg')
        with open(template_file) as f:
            template = f.read()
        template = template.replace("ime_in_priimek", name.encode("utf-8")).replace("kategorija", text.encode("utf-8"))
        return cairosvg.svg2pdf(template)
    
    profile = Profile.objects.get(user__username=username)

    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied

    pdf = _create_mentor_certificate(profile, 'drzavno2015', 'finale2015')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="potrdilo.pdf"'
    response.write(pdf)
    return response


@login_required
def school_awards_pdf(request, username, slug, school_id, cqs_name):
    profile = Profile.objects.get(user__username=username)
    
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_dir = os.path.join(_profile_file_path(profile, 
        os.path.join(slug, school_id)))
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
        #    print e
        # regenerate award. Ignore the template
        template_file = os.path.join(AWARD_TEMPLATE_DIR, 'all_si.svg')
        #print "generating..."
        data = []
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        #print cqs_name
        #for i in profile.schoolteachercode_set.all():
        #    print "  ", i.competition_questionset.name
        #print profile.schoolteachercode_set.filter(school_id = school_id,
        #    competition_questionset__name=cqs_name)
        stcs = profile.schoolteachercode_set.filter(
                    code__codegenerator = competition.competitor_code_generator,
                    competition_questionset__name = cqs_name,
                    school_id = school_id
                ).order_by(
                    'code'
                ).prefetch_related(
                    'code')
        # print stcs
        for stc in stcs:
            stc.assign_si_awards(revoked_by = profile)
            awards = stc.attempt_awards().order_by(
                    'attempt__competitor__last_name',
                    'attempt__competitor__first_name'
                ).select_related(
                    'award')
            for award in awards:
                data.append(
                    {
                        'name': award.competitor_name,
                        'school': award.school_name,
                        'group': award.group_name,
                        'serial': award.serial,
                        'template': award.award.template,
                    }
                )
        generate_award_pdf(cert_full_fname,
            data, template_file)
    #return None
    return safe_media_redirect(cert_path)

@login_required
def all_awards_pdf(request, username, slug, cqs_name):
    profile = Profile.objects.get(user__username=username)
    
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_dir = os.path.join(_profile_file_path(profile, 
        os.path.join(slug)))
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
        #    print e
        # regenerate award. Ignore the template
        template_file = os.path.join(AWARD_TEMPLATE_DIR, 'all_si.svg')
        #print "generating..."
        data = []
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        #print cqs_name
        #for i in profile.schoolteachercode_set.all():
        #    print "  ", i.competition_questionset.name
        #print profile.schoolteachercode_set.filter(school_id = school_id,
        #    competition_questionset__name=cqs_name)
        # print stcs
        awards = AttemptAward.objects.filter(
                attempt__competitionquestionset__competition = competition,
                attempt__competitionquestionset__name = cqs_name,
                revoked_by = None,
            ).order_by(
                'attempt__competitor__last_name',
                'attempt__competitor__first_name'
            ).select_related(
                'award')
        for award in awards:
            data.append(
                {
                    'name': award.competitor_name,
                    'school': award.school_name,
                    'group': award.group_name,
                    'serial': award.serial,
                    'template': award.award.template,
                }
            )
        generate_award_pdf(cert_full_fname,
            data, template_file)
    #return None
    return safe_media_redirect(cert_path)

@login_required
def bla(request):
    pass

def __update_juniorattempt(attempt):
    try:
        j_a = attempt.juniorattempt
        year_class = j_a.year_class
        raw = year_class.raw_data
        lines = raw.split('\n')
        replacement_line = u"{} {}\t{:.0f}".format(
            attempt.competitor.first_name,
            attempt.competitor.last_name,
            attempt.score)
        print (lines[j_a.line],),(replacement_line,)
        lines[j_a.line] = replacement_line
        raw = u"\n".join(lines)
        print raw
        year_class.raw_data = raw
        year_class.save()
    except Exception, e:
        # print e
        pass
   

@login_required
def revalidate_awards(request, attempt_id, *args, **kwargs):
    attempt = get_object_or_404(Attempt, id=attempt_id)
    # TODO check permissions, determine the actual teacher
    teacher = request.profile
    # TODO update all possible awards files containing this attempt
    # print attempt
    __update_juniorattempt(attempt)
    awards_changed = False
    sct = teacher.schoolteachercode_set.get(
        code__value = attempt.access_code,
        competition_questionset = attempt.competitionquestionset
    )
    cqs = sct.competition_questionset
    school = sct.school
    awards_changed = []
    serials = set()
    for aaward in attempt.attemptaward_set.filter(revoked_by = None):
        serials.add(aaward.serial)
        competitor_name = u"{} {}".format(attempt.competitor.first_name,
            attempt.competitor.last_name)
        # print "  ", aaward.competitor_name, competitor_name
        if aaward.competitor_name != competitor_name or \
                aaward.school_name != school.name or \
                aaward.group_name != cqs.name:
            # print "changed!"
            aaward.revoked_by = teacher
            aaward.save()
            aaward.id = None
            aaward.competitor_name = competitor_name
            aaward.school_name = school.name
            aaward.revoked_by = None
            aaward.group_name = cqs.name
            awards_changed.append(aaward)
    for award in awards_changed:
        base_serial = award.serial
        p = base_serial.rfind('-')
        if p >= 0:
            base_serial = base_serial[:p]
        new_serial = base_serial
        i = 1
        # print serials
        while new_serial in serials:
            new_serial = "{}-{}".format(base_serial, i)
            i += 1
        award.serial = new_serial
        # print "created award", award.serial, award, award.revoked_by
        award.save()
        serials.add(new_serial)
    if True or len(awards_changed):
        cert_dir = os.path.join(_profile_file_path(teacher, 
            os.path.join(cqs.competition.slug, str(school.id))))
        cert_fname = cqs.name + '.pdf'
        cert_path = os.path.join(cert_dir, cert_fname)
        cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
        new_cert_full_fname = cert_full_fname
        i = 0
        while os.path.isfile(new_cert_full_fname):
            i += 1
            new_cert_full_fname = u'{}-{}'.format(cert_full_fname, i)
        # print "new file name:", new_cert_full_fname
        os.rename(cert_full_fname, new_cert_full_fname)

    return JsonResponse({'status': 'success'})
