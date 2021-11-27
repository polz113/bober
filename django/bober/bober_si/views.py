import os
from itertools import chain
from openpyxl import Workbook
from collections import defaultdict
from openpyxl.writer.excel import save_virtual_workbook

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Case, When, BooleanField, F

from bober_si.forms import SchoolCodesCreateForm
from bober_simple_competition.views import SmartCompetitionAdminCodeRequiredMixin
from bober_simple_competition.views import safe_media_redirect, _profile_file_path, JsonResponse
from bober_simple_competition.forms import ProfileEditForm
from bober_simple_competition.models import Attempt, Profile, GradedAnswer, AttemptConfirmation

from bober_si.models import SchoolCompetition, CompetitionQuestionSet, Competition, SCHOOL_CATEGORIES, \
    AttemptAward, AWARD_TEMPLATE_DIR
from bober_si.forms import TeacherCodeRegistrationPasswordResetForm
from bober_si.award_gen import generate_award_pdf


class TeacherOverview(SmartCompetitionAdminCodeRequiredMixin,
                      TemplateView):
    template_name = "bober_si/teacher_overview.html"

    def dispatch(self, *args, **kwargs):
        try:
            competition = SchoolCompetition.get_cached_by_slug(slug=kwargs['slug'])
        except Exception:
            # TODO: handle exception
            raise Http404
        access_code = self.request.session['access_code']
        self.competition = competition
        return super(TeacherOverview, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TeacherOverview, self).get_context_data(**kwargs)
        profile = self.request.profile
        context['profile'] = profile
        context['competition'] = self.competition
        context['profile_form'] = ProfileEditForm(instance=profile)
        schools = dict()
        for c in profile.schoolteachercode_set.filter(
                    code__codegenerator=self.competition.competitor_code_generator
                ).order_by(
                    'school__name', 'code'
                ).prefetch_related(
                    'school', 'code',
                ):
            if c.school not in schools:
                # Design decision: there is only one juniormembership per teacher per competition per school.
                junior_mentorship = self.competition.juniormentorship_set.filter(
                    school=c.school,
                    teacher=profile
                ).first()
                schools[c.school] = {
                    "codes": [],
                    "junior_mentorship": junior_mentorship,
                    "attempts": []}
            school = c.school
            code = c.code.value
            sep = self.competition.competitor_code_generator.format.separator
            split_code = code.split(sep)
            cqs_slug = split_code[0]
            cqs = CompetitionQuestionSet.get_by_slug(cqs_slug)
            schools[school]["codes"].append((cqs, sep.join(split_code[1:])))
            all_attempts = Attempt.objects.filter(access_code=code).select_related(
                'competitor',
                'competitionquestionset',
                'competitionquestionset__questionset').prefetch_related(
                'gradedanswer_set',
                'competitionquestionset__questionset__questions',
            ).annotate(
                confirmed=Case(
                    When(confirmed_by__id=profile.id, then=True),
                    default=False, output_field=BooleanField()
                )
            ).order_by('confirmed', 'competitor__last_name', 'competitor__first_name', 'competitor__date_of_birth')
            if all_attempts:
                schools[school]["attempts"].append((cqs, all_attempts))
        context['show_codes'] = self.competition.end >= timezone.now()
        context['show_awards'] = self.competition.end <= timezone.now()
        context['schools'] = schools
        return context


class SchoolCodesCreate(SmartCompetitionAdminCodeRequiredMixin, FormView):
    template_name = "bober_si/school_codes_create.html"
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
    template_name = "bober_si/teacher_registration_password_reset.html"

    def dispatch(self, *args, **kwargs):
        self.competition = Competition.objects.get(slug=kwargs['slug'])
        return super(TeacherCodeRegistrationPasswordReset, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(TeacherCodeRegistrationPasswordReset, self).get_context_data(*args, **kwargs)
        context['hidden_code'] = self.request.GET.get('hidden_code', '')
        print(self.args, self.kwargs)
        context['teacher_login_url'] = reverse("teacher_overview",
                                               kwargs=self.kwargs)
        return context

    def get(self, *args, **kwargs):
        try:
            code = self.competition.administrator_code_generator.codes.get(value=self.request.GET['hidden_code'])
            self.hidden_code = code
        except Exception:
            response = render(self.request, 'bober_si/no_hidden_code.html')
            response.status_code = 403
            return response
        return super(TeacherCodeRegistrationPasswordReset, self).get(*args, **kwargs)

    def get_initial(self):
        initial = super(TeacherCodeRegistrationPasswordReset, self).get_initial()
        initial['hidden_code'] = self.request.GET.get('hidden_code', '')
        return initial

    def form_valid(self, form):
        retval = super(TeacherCodeRegistrationPasswordReset, self).form_valid(form)
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            code = self.competition.administrator_code_generator.codes.get(value=form.cleaned_data['hidden_code'])
        except Exception:
            response = render(self.request, 'bober_si/no_hidden_code.html')
            response.status_code = 403
            return response
        try:
            assert not User.objects.filter(email=email).exists()
            assert not User.objects.filter(username=username).exists()
            user = User(username=username, email=email)
        except Exception:
            # TODO: handle exception
            response = render(self.request, 'bober_si/no_hidden_code.html')
            response.status_code = 403
            return response
        user.set_password(password)
        user.save()
        user.profile.managed_profiles.add(user.profile)
        user.profile.received_codes.add(code)
        u = authenticate(username=user.username, password=password)
        login(self.request, u)
        return retval

    def get_success_url(self):
        return reverse('teacher_overview', kwargs={"slug": self.competition.slug})


class ProfilesBySchoolCategory(SmartCompetitionAdminCodeRequiredMixin, TemplateView):
    template_name = 'bober_si/profiles_by_schooltype.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilesBySchoolCategory, self).get_context_data(*args, **kwargs)
        categories = dict()
        for category in SCHOOL_CATEGORIES:
            profiles = Profile.objects.filter(
                schoolteachercode__school__category=category[0],
                schoolteachercode__code__codegenerator=self.competition.competitor_code_generator,
            ).distinct()
            if profiles.count() > 0:
                categories[category] = profiles
        context['categories'] = categories
        return context

    def dispatch(self, *args, **kwargs):
        self.competition = SchoolCompetition.objects.get(slug=kwargs.pop('slug'))
        if not self.competition.administrator_code_generator.code_matches(
                self.access_code,
                {'admin_privileges': ['view_all_competitor_codes']}):
            print ("No view_all_competitor_codes privilege")
            raise PermissionDenied
        return super(ProfilesBySchoolCategory, self).dispatch(*args, **kwargs)


class CompetitionXlsResults(SmartCompetitionAdminCodeRequiredMixin, TemplateView):
    template_name = 'bober_si/competition_results.xls'

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.excel_results(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    def excel_results(self):
        def profiles_str(p_list):
            return u", ".join([
                u"{} <{}>".format(
                    i.user.username, i.user.email
                ) for i in p_list])
        wb = Workbook()
        ws = wb.active
        for cqs in self.competitionquestionsets.all():
            # t0 = datetime.datetime.now()
            profiles_by_code = defaultdict(list)
            schools_by_code = defaultdict(list)
            schools_by_teacher = defaultdict(list)
            for code in self.competition.competitor_code_generator.codes.filter(
                    value__startswith=cqs.slug_str()):
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
                'Duration',
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
            gradedanswers = dict()
            for attempt_id, question_id, score in GradedAnswer.objects.filter(
                        attempt__competitionquestionset__id=cqs.id
                    ).distinct().values_list(
                        'attempt_id', 'question_id', 'score'):
                gradedanswers[(attempt_id, question_id)] = score
            confirmations = defaultdict(list)
            for by_id, attempt_id, username, email in AttemptConfirmation.objects.filter(
                        attempt__competitionquestionset__id=cqs.id
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
            for attempt_id, revoked_by, award_name, award_serial in AttemptAward.objects.filter(
                        attempt__competitionquestionset__id=cqs.id
                    ).distinct().values_list('attempt_id',
                                             'revoked_by',
                                             'award__name', 'serial'):
                if revoked_by is not None:
                    revoked_awards[attempt_id].append("{}: {}".format(award_name, award_serial))
                else:
                    awards[attempt_id].append("{}: {}".format(award_name, award_serial))
            attempts = cqs.attempt_set.all()
            for (
                    attempt_id,
                    attempt_start,
                    attempt_finish,
                    attempt_duration,
                    access_code,
                    first_name,
                    last_name,
                    date_of_birth,
                    attempt_score,
                ) in attempts.values_list(
                    'id',
                    'start',
                    'finish',
                    'duration',
                    'access_code',
                    'competitor__first_name',
                    'competitor__last_name',
                    'competitor__date_of_birth',
                    'score').distinct():
                # print "  attempt:", attempt.id
                mentors = profiles_by_code[access_code]
                schools = schools_by_code[access_code]
                confirmed_schools = set()
                confirmed_by = confirmations[attempt_id]
                for p in confirmed_by:
                    for s in schools_by_teacher[p[0]]:
                        confirmed_schools.add(s)
                confirmed_by_schools = set(schools).intersection(
                    confirmed_schools)
                attempt_start = attempt_start.replace(tzinfo=None)
                if attempt_finish is not None: 
                    attempt_finish = attempt_finish.replace(tzinfo=None)
                l1 = [
                    attempt_id,
                    attempt_start,
                    attempt_finish,
                    attempt_duration,
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
                ws.append(l1)
            ws = wb.create_sheet()
        return save_virtual_workbook(wb)

    def dispatch(self, *args, **kwargs):
        self.competition = SchoolCompetition.get_cached_by_slug(slug=kwargs.pop('slug'))
        if not self.competition.administrator_code_generator.code_matches(
                self.request.session['access_code'],
                {'admin_privileges': ['view_all_competitor_codes']}):
            raise PermissionDenied
        self.competitionquestionsets = CompetitionQuestionSet.objects.filter(
            competition=self.competition)
        cqs_id = kwargs.pop('cqs_id', None)
        if cqs_id is not None:
            self.competitionquestionsets = self.competitionquestionsets.filter(id=cqs_id)
        return super(CompetitionXlsResults, self).dispatch(*args, **kwargs)


@login_required
def mentor_recognition_pdf(request, slug, username):
    profile = Profile.objects.get(user__username=username)
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_fname = "bober-potrdilo-{}.pdf".format(slug)
    cert_dir = _profile_file_path(profile, slug)
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
    cert_full_fname = os.path.join(cert_full_dir, cert_fname)
    try:
        assert os.path.isfile(cert_full_fname)
    except Exception:
        # TODO: handle exception
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        try:
            os.makedirs(cert_full_dir)
        except Exception as e:
            # TODO: handle exception
            pass
        try:
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, competition.slug)
            assert os.path.isdir(template_dir)
        except Exception:
            # TODO: handle exception
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, 'default')
        data = []
        for recognition in profile.teacherrecognition_set.filter(
                template__competition=competition, revoked_by=None):
            d = {'text': recognition.text,
                 'serial': recognition.serial,
                 'name': recognition.recipient,
                 'template': recognition.template.template
                 }
            data.append(d)
        generate_award_pdf(cert_full_fname, data, template_dir)
    return safe_media_redirect(cert_path)


@login_required
def school_awards_pdf(request, username, slug, school_id, cqs_name):
    profile = Profile.objects.get(user__username=username)
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_dir = os.path.join(_profile_file_path(
        profile, os.path.join(slug, school_id, 'all')))
    cert_fname = cqs_name + '.pdf'
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
    try:
        assert False
        assert os.path.isfile(cert_full_fname)
    except Exception:
        # TODO: handle exception
        try:
            cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
            os.makedirs(cert_full_dir)
        except Exception as e:
            # TODO: handle exception
            pass
        data = []
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        stcs = profile.schoolteachercode_set.filter(
                    code__codegenerator=competition.competitor_code_generator,
                    competition_questionset__name=cqs_name,
                    school_id=school_id
                ).order_by(
                    'code'
                ).prefetch_related(
                    'code')
        # print stcs
        for stc in stcs:
            stc.assign_si_awards(revoked_by=profile)
            awards = stc.attempt_awards().order_by(
                    'attempt__competitor__last_name',
                    'attempt__competitor__first_name'
                ).select_related(
                    'award')
            for award in awards:
                data.append(
                    {
                        'name': award.competitor_name,
                        'competition': award.attempt.competitionquestionset.competition,
                        'group': award.attempt.competitionquestionset.name,
                        'school': award.school_name,
                        'group': award.group_name,
                        'serial': award.serial,
                        'template': award.award.template,
                    }
                )
        try:
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, competition.slug)
            assert os.path.isdir(template_dir)
        except Exception:
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, 'default')
            # TODO: handle exception
        generate_award_pdf(cert_full_fname, data, template_dir)
    return safe_media_redirect(cert_path)


@login_required
def awards_school_type_pdf(request, username,
                           slug, school_id, award_name, cqs_name):
    profile = Profile.objects.get(user__username=username)
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_dir = os.path.join(_profile_file_path(
        profile, os.path.join(slug, school_id, 'by_type', award_name)))
    cert_fname = cqs_name + '.pdf'
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
    try:
        # print "f:", os.path.join(settings.MEDIA_ROOT, cert_path)
        assert os.path.isfile(cert_full_fname)
    except Exception:
        # TODO: handle exception
        try:
            cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
            os.makedirs(cert_full_dir)
        except Exception as e:
            # TODO: handle exception
            pass
        data = []
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        stcs = profile.schoolteachercode_set.filter(
                    code__codegenerator=competition.competitor_code_generator,
                    competition_questionset__name=cqs_name,
                    school_id=school_id
                ).order_by(
                    'code'
                ).prefetch_related(
                    'code')
        for stc in stcs:
            stc.assign_si_awards(revoked_by=profile)
            awards = stc.attempt_awards().filter(
                    award__name=award_name
                ).order_by(
                    'attempt__competitor__last_name',
                    'attempt__competitor__first_name'
                ).select_related(
                    'award')
            for award in awards:
                data.append(
                    {
                        'name': award.competitor_name,
                        'competition': award.attempt.competitionquestionset.competition,
                        'group': award.attempt.competitionquestionset.name,
                        'school': award.school_name,
                        'group': award.group_name,
                        'serial': award.serial,
                        'template': award.award.template,
                    }
                )
        try:
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, competition.slug)
            assert os.path.isdir(template_dir)
        except Exception:
            # TODO: handle exception
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, 'default')
        generate_award_pdf(cert_full_fname, data, template_dir)
    return safe_media_redirect(cert_path)


@login_required
def awards_type_pdf(request, username, slug, award_name, cqs_name):
    profile = Profile.objects.get(user__username=username)
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_dir = os.path.join(_profile_file_path(
        profile, os.path.join(slug, 'by_type', award_name)))
    cert_fname = cqs_name + '-' + award_name + '.pdf'
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
    try:
        # print "f:", os.path.join(settings.MEDIA_ROOT, cert_path)
        assert os.path.isfile(cert_full_fname)
    except Exception:
        # TODO: handle exception
        try:
            cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
            os.makedirs(cert_full_dir)
        except Exception as e:
            # TODO: handle exception
            pass
        data = []
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        awards = AttemptAward.objects.filter(
                attempt__competitionquestionset__competition=competition,
                attempt__competitionquestionset__name=cqs_name,
                award__name=award_name,
                revoked_by=None,
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
                    # 'date': '7. - 11. novembra 2016',
                    'serial': award.serial,
                    'template': award.award.template,
                }
            )
        try:
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, competition.slug)
            assert os.path.isdir(template_dir)
        except Exception:
            # TODO: handle exception
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, 'default')
        generate_award_pdf(cert_full_fname, data, template_dir)
    return safe_media_redirect(cert_path)


@login_required
def all_awards_pdf(request, username, slug, cqs_name):
    profile = Profile.objects.get(user__username=username)
    if profile.user != request.user and \
            request.profile.managed_profiles.filter(
                id=profile.id).count() <= 0:
        raise PermissionDenied
    cert_dir = os.path.join(_profile_file_path(profile, os.path.join(slug)))
    cert_fname = cqs_name + '.pdf'
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
    try:
        assert os.path.isfile(cert_full_fname)
    except Exception:
        # TODO: handle exception
        try:
            cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
            os.makedirs(cert_full_dir)
        except Exception as e:
            # TODO: handle exception
            pass
        data = []
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        awards = AttemptAward.objects.filter(
                attempt__competitionquestionset__competition=competition,
                attempt__competitionquestionset__name=cqs_name,
                revoked_by=None,
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
                    # 'date': '7. - 11. novembra 2016',
                    'serial': award.serial,
                    'template': award.award.template,
                }
            )
        try:
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, competition.slug)
            assert os.path.isdir(template_dir)
        except Exception:
            # TODO: handle exception
            template_dir = os.path.join(AWARD_TEMPLATE_DIR, 'default')
        generate_award_pdf(cert_full_fname, data, template_dir)
    return safe_media_redirect(cert_path)


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
        lines[j_a.line] = replacement_line
        raw = u"\n".join(lines)
        year_class.raw_data = raw
        year_class.save()
    except Exception as e:
        # TODO: handle exception
        pass


@login_required
def revalidate_awards(request, attempt_id, *args, **kwargs):
    attempt = get_object_or_404(Attempt, id=attempt_id)
    # TODO check permissions, determine the actual teacher
    teacher = request.profile
    # TODO update all possible awards files containing this attempt
    # print attempt
    __update_juniorattempt(attempt)
    sct = teacher.schoolteachercode_set.get(
        code__value=attempt.access_code,
        competition_questionset=attempt.competitionquestionset
    )
    cqs = sct.competition_questionset
    school = sct.school
    awards_changed = []
    serials = set()
    for aaward in attempt.attemptaward_set.filter(revoked_by=None):
        serials.add(aaward.serial)
        competitor_name = u"{} {}".format(attempt.competitor.first_name, attempt.competitor.last_name)
        if aaward.competitor_name != competitor_name or \
                aaward.school_name != school.name or \
                aaward.group_name != cqs.name:
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
        while new_serial in serials:
            new_serial = "{}-{}".format(base_serial, i)
            i += 1
        award.serial = new_serial
        award.save()
        serials.add(new_serial)
    if len(awards_changed):
        cert_dir = os.path.join(_profile_file_path(teacher, os.path.join(cqs.competition.slug, str(school.id))))
        cert_fname = cqs.name + '.pdf'
        cert_path = os.path.join(cert_dir, cert_fname)
        cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
        new_cert_full_fname = cert_full_fname
        i = 0
        while os.path.isfile(new_cert_full_fname):
            i += 1
            new_cert_full_fname = u'{}-{}'.format(cert_full_fname, i)
        if os.path.isfile(cert_full_fname):
            os.rename(cert_full_fname, new_cert_full_fname)

    return JsonResponse({'status': 'success'})
