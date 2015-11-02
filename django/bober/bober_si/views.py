from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from forms import OverviewForm, SchoolCodesCreateForm
from bober_simple_competition.views import AccessCodeRequiredMixin, SmartCompetitionAccessCodeRequiredMixin
from bober_simple_competition.models import Attempt
from models import *
from braces.views import LoginRequiredMixin
# Create your views here.

class TeacherOverview(SmartCompetitionAccessCodeRequiredMixin, 
        TemplateView):
    template_name="bober_si/teacher_overview.html"
    def get_context_data(self, **kwargs):
        context = super(TeacherOverview, self).get_context_data(**kwargs)
        profile = self.request.user.profile
        context['profile'] = profile 
        competition = SchoolCompetition.objects.get(slug=kwargs['slug'])
        context['competition'] = competition
        school = None
        schools = dict()
        attempts = dict()
        code_pairs = list()
        for c in profile.schoolteachercode_set.order_by(
                'school', 'code__value'):
            if c.school != school:
                schools[c.school] = list()
                attempts[c.school] = list()
            school = c.school
            code = c.code.value
            sep = competition.competitor_code_generator.format.separator
            split_code = code.split(sep)
            cqs_slug = split_code[0]
            cqs = CompetitionQuestionSet.get_by_slug(cqs_slug)
            schools[school].append((cqs, sep.join(split_code[1:])))
            attempts[school].append((cqs, Attempt.objects.filter(access_code = code)))
        context['schools'] = schools
        context['attempts'] = attempts
        # print attempts
        return context

class SchoolCodesCreate(LoginRequiredMixin, AccessCodeRequiredMixin, FormView):
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
