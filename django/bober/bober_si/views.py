from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from forms import OverviewForm, SchoolCodesCreateForm
from bober_simple_competition.views import AccessCodeRequiredMixin, SmartCompetitionAdminCodeRequiredMixin
from bober_simple_competition.models import Attempt, Profile
from bober_paper_submissions.models import JuniorDefaultYear
from django.contrib.auth.models import User
from models import *
from forms import *
from collections import OrderedDict
from braces.views import LoginRequiredMixin
# Create your views here.


class TeacherOverview(SmartCompetitionAdminCodeRequiredMixin, 
        TemplateView):
    template_name="bober_si/teacher_overview.html"

    def dispatch(self, *args, **kwargs):
        competition = SchoolCompetition.objects.get(slug=kwargs['slug'])
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
        show_paper_results = False
        for c in profile.schoolteachercode_set.filter(
                    code__salt = self.competition.competitor_code_generator.salt,
                    code__format = self.competition.competitor_code_generator.format, 
                ).order_by(
                    'school', 'code__value'):
            if c.school != school:
                schools[c.school] = []
                attempts[c.school] = []
            school = c.school
            show_paper_results |= JuniorDefaultYear.objects.filter(
                competition = self.competition,
                school_category = school.category,
                ).count() > 0
            code = c.code.value
            sep = self.competition.competitor_code_generator.format.separator
            split_code = code.split(sep)
            cqs_slug = split_code[0]
            cqs = CompetitionQuestionSet.get_by_slug(cqs_slug)
            schools[school].append((cqs, sep.join(split_code[1:])))
            a_list = []
            for a in Attempt.objects.filter(
                    access_code = code).prefetch_related('gradedanswer_set'):
                if a.confirmed_by.filter(id=profile.id).count() > 0:
                    a_list.append((a, 'confirmed'))
                else:
                    a_list.append((a, 'unconfirmed'))
            attempts[school].append((cqs, a_list))
        context['show_paper_results'] = show_paper_results
        context['schools'] = schools
        context['attempts'] = attempts
        context['junior_mentorships'] = profile.juniormentorship_set.filter(
            competition = self.competition)
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
