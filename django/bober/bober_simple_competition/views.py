import datetime
import time
import json
import random
import string
import email.utils
import os
import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView,\
    UpdateView, FormView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django import forms
from django.db.models import Q

from django_tables2 import SingleTableView
from braces.views import LoginRequiredMixin
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from dal import autocomplete
from popup_modelviews.views import\
    PopupUpdateView, PopupCreateView, PopupFormViewMixin,\
    InvalidFormRespond422

import code_based_auth.models
from bober_simple_competition.forms import\
    MailForm, CompetitorCodeFormatForm,\
    CompetitorUpdateForm, ProfileEditForm,\
    ProfileMergeForm, QuestionSetRegistrationForm,\
    CompetitionRegistrationForm, AdminCodeFormatForm, MinimalAccessCodeForm,\
    QuestionSetCompetitorForm, CompetitionCompetitorForm,\
    QuestionSetForm, CompetitionUpdateForm, CompetitionCreateForm,\
    CompetitionQuestionSetUpdateInline, CompetitionQuestionSetCreateInline
from bober_simple_competition import tables
from bober_simple_competition import filters
from bober_simple_competition.models import\
    Profile, Competition, CompetitionQuestionSet, Resource,\
    QuestionSet, Code, Question, Attempt, Competitor,\
    ADMIN_PRIVILEGES, COMPETITOR_PRIVILEGES, CODE_EFFECTS,\
    graders, Answer, GradedAnswer, AttemptConfirmation


def send_email(request):
    mail_users = request.GET.getlist('select')
    emails = request.profile.managed_profiles.filter(
        pk__in=mail_users
    ).values_list('user__email', flat=True)
    form = MailForm(initial={'mail_to': ", ".join(emails)})
    return render(
        request,
        'bober_simple_competition/send_email.html', {'form': form})


def send_to_mail(request):
    logger = logging.getLogger(__name__)
    if request.method == 'GET':
        mail_form = MailForm(data=request.GET)
        if mail_form.is_valid():
            mail_from = request.profile.user.email
            mail_to = mail_form.cleaned_data['mail_to']
            mail_to_list = [
                i[1] for i in email.utils.getaddresses([mail_to])
            ]
            subject = mail_form.cleaned_data['mail_subject']
            mail_content = mail_form.cleaned_data['mail_content']
            logger.debug("Send email with subject {} from {}".format(
                subject, mail_from))
            logger.debug("Mail to: {}".format(mail_to_list))
            logger.debug("Mail content: {}".format(mail_content))
            msg = EmailMultiAlternatives(subject, mail_content, mail_from,
                                         mail_to_list)
            msg.send()
    return redirect("/simple/users")


# get rid of this when we stop supporting django 1.5
def JsonResponse(data, **kwargs):
    return HttpResponse(json.dumps(data), content_type='application/json',
                        **kwargs)


class OutOfTimeError(Exception):
    pass


def access_code_required(function=None):
    """
    Decorator requiring access code to proceed.
    """
    def wrap(*args, **kwargs):
        request = kwargs.get('request', args[0])
        if "access_code" in request.session:
            return function(*args, **kwargs)
        else:
            return redirect('access_code', url_next=request.get_full_path())
    return wrap


def smart_competition_admin_code_required(function=None):
    """Try to find an access code this user already has before asking for it"""
    def code_fn(*args, **kwargs):
        request = kwargs.get('request', args[0])
        access_code = request.session.get('access_code', None)
        try:
            competition = Competition.get_cached_by_slug(slug=kwargs['slug'])
            codegen = competition.administrator_code_generator
            codes = []
            if access_code is not None:
                codes = codegen.codes.filter(
                    value=access_code).values_list('value', flat=True)
            if not codes and access_code is not None\
                    and codegen.code_matches(
                        access_code,
                        {'competitor_privileges': ['attempt']}):
                codes = [codegen.format.canonical_code(access_code)]
            if not codes:
                codes = codegen.codes.filter(
                    recipient_set__id=request.profile.id).values_list(
                        'value', flat=True)
            if not codes:
                codes = codegen.codes.filter(
                    user_set__id=request.profile.id).values_list(
                        'value', flat=True)
            if not codes:
                codes = codegen.codes.filter(
                    creator_set__id=request.profile.id).values_list(
                        'value', flat=True)
            access_code = codes[0]
        except Exception:
            logger = logging.getLogger(__name__)
            logger.exception("smart_competition_admin_code_required")
            pass
        if access_code is not None:
            _use_access_code(request, access_code)
        else:
            _next = request.get_full_path()
            return redirect('access_code', url_next=_next)
        return function(*args, **kwargs)
    return login_required(code_fn)


class AccessCodeRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AccessCodeRequiredMixin, cls).as_view(**initkwargs)
        return access_code_required(view)


class SmartCompetitionAdminCodeRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(SmartCompetitionAdminCodeRequiredMixin,
                     cls).as_view(**initkwargs)
        return smart_competition_admin_code_required(view)


class FilteredSingleTableView(SingleTableView):
    filter_class = None

    def get_table_data(self):
        self.filter = self.filter_class(
            self.request.GET,
            queryset=super(FilteredSingleTableView, self).get_table_data())
        return self.filter

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context


def _use_access_code(request, access_code,
                     defer_update_used_codes=False,
                     defer_code_effects=False):
    request.session['access_code'] = access_code
    # print access_code, defer_update_used_codes, defer_code_effects
    try:
        if not defer_update_used_codes:
            profile = request.profile
            code = Code.objects.get(value=access_code)
            profile.used_codes.add(code)
    except Exception as e:
        # TODO: add exception handling
        pass
    try:
        if not defer_code_effects:
            profile = request.profile
            for effect in code.codeeffect_set.all():
                effect.apply(users=[profile])
    except Exception as e:
        # TODO: add exception handling
        pass


class CodeAutocomplete(autocomplete.Select2QuerySetView):
    model = Code

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Code.objects.none()
        if self.request.user.is_superuser:
            return Code.objects.all()
        # TODO: add filtering by creator / recipient / user
        qs = Code.objects.filter(Q(recipient_set=self.request.profile) |
                                 Q(user_set=self.request.profile) |
                                 Q(creator_set=self.request.profile))
        return qs


def access_code(request, url_next):
    qd = QueryDict(dict(), mutable=True)
    qd.update(request.GET)
    qd.update(request.POST)
    if len(qd):
        form = MinimalAccessCodeForm(qd)
    else:
        form = MinimalAccessCodeForm()
    if form.is_valid():
        defer_update = form.cleaned_data.get('defer_update_used_codes', False)
        defer_effects = form.cleaned_data.get('defer_effects', False)
        access_code = form.cleaned_data['access_code']
        _use_access_code(request, access_code, defer_update, defer_effects)
        return HttpResponseRedirect('/' + url_next)
    return render(
        request,
        'bober_simple_competition/access_code.html', locals())


def competitionquestionset_access_code(request, competition_questionset_id,
                                       url_next):
    qd = QueryDict(dict(), mutable=True)
    qd.update(request.GET)
    qd.update(request.POST)
    if len(qd):
        form = MinimalAccessCodeForm(qd)
    else:
        form = MinimalAccessCodeForm()
    if 'access_code' in request.session and 'access_code' not in qd:
        qd['access_code'] = request.session['access_code']
    try:
        cqs = CompetitionQuestionSet.objects.get(
            id=competition_questionset_id)
        cqs_slug = cqs.slug_str()
        code_format = cqs.competition.competitor_code_generator.format
    except Exception as e:
        cqs_slug = None
    if cqs_slug is not None and form.is_valid():
        defer_update = form.cleaned_data.get('defer_update_used_codes', False)
        defer_effects = form.cleaned_data.get('defer_effects', False)
        short_access_code = form.cleaned_data['access_code']
        request.session['short_access_code'] = short_access_code
        access_code = cqs_slug + code_format.separator + short_access_code
        access_code = code_format.canonical_code(access_code)
        _use_access_code(request, access_code, defer_update, defer_effects)
        # print "    ", request.session['access_code']
        return redirect(url_next)
    return render(
        request,
        'bober_simple_competition/access_code.html', locals())


def index(request):
    """
    When there is exactly one ongoing promoted competition show
    login page, otherwise redirect to the competition list page.
    """
    promoted = Competition.ongoing_competitions().filter(promoted=True)
    if promoted.count() == 1:
        competition = promoted.get()
        return redirect('competition_compete_promoted', slug=competition.slug)
    else:
        return redirect('competition_list')


class CompetitionList(ListView):
    model = Competition
    queryset = Competition.objects.filter(public=True).order_by('-promoted', '-start')

    def get(self, *args, **kwargs):
        if hasattr(self.request, 'profile'):
            profile = self.request.profile
            if not profile.user.first_name or not profile.user.last_name or not profile.user.email:
                return redirect('profile_update', profile.id)
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Separate competitions into three groups:
        - promoted (current)
        - old
        - available for guests
        """
        context = super(CompetitionList, self).get_context_data(**kwargs)
        competitions = context['object_list']
        context['promoted'] = competitions.filter(promoted=True)
        regular = competitions.filter(promoted=False)
        context['guests_allowed'] = [c for c in regular if c.guests_allowed]
        context['old'] = [c for c in regular if not c.guests_allowed]
        return context


class GuestCompetitionList(ListView):
    model = Competition
    template_name = "bober_simple_competition/guest_competitions.html"
    queryset = Competition.objects.filter(
            public=True, competitionquestionset__guest_code__isnull=False
        ).order_by('-promoted', '-start').distinct()


class GuestCompetitionQuestionSetList(ListView):
    model = CompetitionQuestionSet
    template_name = "bober_simple_competition/guest_questionsets.html"

    def get_queryset(self):
        self.competition = get_object_or_404(Competition,
                                             slug=self.kwargs['slug'])
        return CompetitionQuestionSet.objects.filter(
            competition=self.competition, guest_code__isnull=False)

    def get_context_data(self, **kwargs):
        context = super(GuestCompetitionQuestionSetList, self).get_context_data(**kwargs)
        context['competition'] = self.competition
        return context


class CompetitionDetail(DetailView):
    model = Competition


class CompetitionUpdate(SmartCompetitionAdminCodeRequiredMixin,
                        UpdateWithInlinesView):
    model = Competition
    form_class = CompetitionUpdateForm
    inlines = [CompetitionQuestionSetUpdateInline]

    def get_object(self, queryset=None):
        c = super(CompetitionUpdate, self).get_object(queryset)
        access_code = self.request.session['access_code']
        if not c.administrator_code_generator.code_matches(
                access_code,
                {'admin_privileges': ['modify_competition']}):
            raise PermissionDenied
        return c

    def forms_valid(self, form, inlines):
        retval = super(CompetitionUpdate, self).forms_valid(form, inlines)
        if not retval:
            return retval
        for i in inlines:
            for f in i.forms:
                if not f.empty_permitted and f.is_valid():
                    f.save()
                    if f.new_code_created:
                        # print "Creating guest code!"
                        self.request.profile.created_codes.add(
                            f.instance.guest_code)
                    # print f.instance, f.cleaned_data['create_guest_code']
        return retval


# 8. create competition (from multiple questionsets)
#   all questionsets for competitions you have admin access to can be used.
#   Also, newly created questionsets can be used.
class CompetitionCreate(LoginRequiredMixin, CreateWithInlinesView):
    model = Competition
    form_class = CompetitionCreateForm
    inlines = [CompetitionQuestionSetCreateInline]

    def forms_valid(self, form, inlines):
        # print "Creating new competition after retval!"
        admin_codegen = code_based_auth.models.CodeGenerator(
            unique_code_component='code_id',
            format=form.cleaned_data['admin_code_format'],
            salt=form.cleaned_data['admin_salt'])
        admin_codegen.save()
        competitor_codegen = code_based_auth.models.CodeGenerator(
            unique_code_component='code_id',
            format=form.cleaned_data['competitor_code_format'],
            salt=form.cleaned_data['competitor_salt'])
        competitor_codegen.save()
        competition = form.instance
        competition.administrator_code_generator = admin_codegen
        competition.competitor_code_generator = competitor_codegen
        competition.save()
        master_code = competition.master_code_create()
        self.request.profile.received_codes.add(master_code)
        self.request.profile.created_codes.add(master_code)
        retval = super(CompetitionCreate, self).forms_valid(form, inlines)
        for i in inlines:
            for f in i.forms:
                if f.cleaned_data.get('create_guest_code', False) and \
                        hasattr(f.instance, 'guest_code') and \
                        f.instance.guest_code is None:
                    f.instance.save()
                    code_data = {
                        'competitor_privileges': [
                            'attempt', 'results_before_end', 'new_attempt'
                        ],
                        'competition_questionset': [f.instance.slug_str()]
                    }
                    c = competitor_codegen.create_code(code_data)
                    f.instance.guest_code = c
                    f.instance.save()
        return retval

    def get_initial(self):
        return {
            'admin_code_format':
                (code_based_auth.models.CodeFormat.objects.filter(
                    components__name='admin_privileges'
                ).order_by('id')[:1] or [None])[0],
            'competitor_code_format':
                (code_based_auth.models.CodeFormat.objects.filter(
                    components__name='competition_questionset'
                ).order_by('id')[:1] or [None])[0],
            'admin_salt': ''.join([
                random.choice(string.ascii_letters+string.digits)
                for _ in range(10)]),
            'competitor_salt': ''.join([
                random.choice(string.ascii_letters+string.digits)
                for _ in range(10)]),
            }


class AdminCodeFormatList(ListView, LoginRequiredMixin):
    model = code_based_auth.models.CodeFormat
    template_name = "bober_simple_competition/codeformat_list.html"
    queryset = code_based_auth.models.CodeFormat.objects.filter(
        components__name='admin_privileges')


class CompetitorCodeFormatList(ListView, LoginRequiredMixin):
    model = code_based_auth.models.CodeFormat
    template_name = "bober_simple_competition/codeformat_list.html"
    queryset = code_based_auth.models.CodeFormat.objects.filter(
        components__name='competition_questionset')


class CodeFormatDetail(FormView, LoginRequiredMixin):
    model = code_based_auth.models.CodeFormat


class AdminCodeFormatCreate(FormView, LoginRequiredMixin):
    form_class = AdminCodeFormatForm
    template_name = "bober_simple_competition/codeformat_create.html"

    def get_success_url(self):
        return reverse("admin_code_format_list")

    def form_valid(self, form):
        code_components = [
            {
                'name': 'code_id',
                'hash_len': form.cleaned_data['code_id_length'],
                'hash_format': form.cleaned_data['code_id_format'],
                'hash_algorithm': 'noop',
                'max_parts': 1,
            },
            {
                'name': 'competitor_privileges',
                'hash_len': form.cleaned_data['competitor_privilege_length'],
                'hash_format': form.cleaned_data['competitor_privilege_format'],
                'hash_algorithm': form.cleaned_data['competitor_privilege_hash'],
                'max_parts': len(COMPETITOR_PRIVILEGES),
            },
            {
                'name': 'admin_privileges',
                'hash_len': form.cleaned_data['admin_privilege_length'],
                'hash_format': form.cleaned_data['admin_privilege_format'],
                'hash_algorithm': form.cleaned_data['admin_privilege_hash'],
                'max_parts': len(ADMIN_PRIVILEGES),
            },
            {
                'name': 'allowed_effects',
                'hash_len': form.cleaned_data['allowed_effects_length'],
                'hash_format': form.cleaned_data['allowed_effects_format'],
                'hash_algorithm': form.cleaned_data['allowed_effects_hash'],
                'max_parts': len(CODE_EFFECTS),
            },
        ]
        code_based_auth.models.CodeFormat.from_components(code_components)
        return super(AdminCodeFormatCreate, self).form_valid(form)


class CompetitorCodeFormatCreate(FormView, LoginRequiredMixin):
    form_class = CompetitorCodeFormatForm
    template_name = "bober_simple_competition/codeformat_create.html"

    def get_success_url(self):
        return reverse("competitor_code_format_list")

    def form_valid(self, form):
        code_components = [
            {
                'name': 'competition_questionset',
                'hash_len': 64,  # 50 for slug, 1 for ., 13 for ID.
                'hash_format': 'r',
                'hash_algorithm': form.cleaned_data['questionset_hash'],
                'max_parts': 1,
            },
            {
                'name': 'code_id',
                'hash_len': form.cleaned_data['code_id_length'],
                'hash_format': form.cleaned_data['code_id_format'],
                'hash_algorithm': 'noop',
                'max_parts': 1,
            },
            {
                'name': 'competitor_privileges',
                'hash_len': form.cleaned_data['competitor_privilege_length'],
                'hash_format': form.cleaned_data['competitor_privilege_format'],
                'hash_algorithm': form.cleaned_data['competitor_privilege_hash'],
                'max_parts': len(COMPETITOR_PRIVILEGES),
            },
        ]
        code_based_auth.models.CodeFormat.from_components(code_components)
        return super(CompetitorCodeFormatCreate, self).form_valid(form)


@login_required
def competition_code_list(request, slug):
    competition = Competition.objects.get(slug=slug)
    admin_codegen = competition.administrator_code_generator
    try:
        access_code = request.session['access_code']
    except KeyError:
        access_code = ""
    admin_codes = admin_codegen.codes.all().distinct()
    all_competitor_codes = competition.competitor_code_generator.codes.all().distinct()
    if not admin_codegen.code_matches(
            access_code, {'admin_privileges': ['view_all_admin_codes']}):
        admin_codes = admin_codes.filter(
            Q(creator_set=request.profile)
            | Q(recipient_set=request.profile)
            | Q(user_set=request.profile))
    else:
        print("Have permission to view admin codes")
    if not admin_codegen.code_matches(
            access_code, {'admin_privileges': ['view_all_competitor_codes']}):
        all_competitor_codes = all_competitor_codes.filter(
            Q(creator_set=request.profile)
            | Q(recipient_set=request.profile)
            | Q(user_set=request.profile))
    else:
        print("Have permission to view competitor codes")
        print("    codes:", all_competitor_codes)
    competitor_codes = dict()
    for cqs in CompetitionQuestionSet.objects.filter(competition=competition):
        c_list = list()
        cqs_slug = cqs.slug_str()
        slugpart_len = len(cqs_slug) \
            + len(competition.competitor_code_generator.format.separator)
        for c in all_competitor_codes.filter(value__startswith=cqs_slug):
            c_list.append(c.value[slugpart_len:])
        competitor_codes[cqs] = c_list
    can_create_administrator_codes = admin_codegen.code_matches(
        access_code, {'admin_privileges': ['create_admin_codes']})
    # print access_code, can_create_administrator_codes
    can_create_competitor_codes = admin_codegen.code_matches(
        access_code, {'admin_privileges': ['create_competitor_codes']})
    return render(
        request, "bober_simple_competition/competition_code_list.html",
        locals())


# codes can have the following permissions:
# 1. can create admin codes for this competition
# 2. can create teacher codes for this competition
# 3. can create student codes for this competition
# 4. can attempt competition
# 5. can attempt competition before official start
# 6. can view results before official end
# 7. can use questionset to create new competitions
@smart_competition_admin_code_required
def competition_code_create(request, slug, user_type='admin'):
    access_code = request.session['access_code']
    competition = get_object_or_404(Competition, slug=slug)
    admin_codegen = competition.administrator_code_generator
    competitor_privilege_choices = competition.competitor_privilege_choices(
        access_code)
    allowed_effect_choices = competition.allowed_effect_choices(access_code)
    admin_privilege_choices = list()
    if user_type == 'admin':
        if not admin_codegen.code_matches(
                access_code,
                {'admin_privileges': ['create_admin_codes']}):
            raise PermissionDenied
        admin_privilege_choices = competition.admin_privilege_choices(
            access_code)
        generator = admin_codegen

        class FormClass(forms.Form):
            competitor_privileges = forms.MultipleChoiceField(
                choices=competitor_privilege_choices,
                widget=forms.CheckboxSelectMultiple(),
                required=False, label=_("Competitior privileges"))
            admin_privileges = forms.MultipleChoiceField(
                choices=admin_privilege_choices,
                widget=forms.CheckboxSelectMultiple(),
                required=False, label=_("Admin privileges"))
            allowed_effects = forms.MultipleChoiceField(
                choices=allowed_effect_choices,
                widget=forms.CheckboxSelectMultiple(),
                required=False, label=_("Allowed effects"))
            code_effects = forms.MultipleChoiceField(
                choices=allowed_effect_choices,
                widget=forms.CheckboxSelectMultiple(),
                required=False, label=_("Code effects"))
    else:  # user_type == 'competitor'
        generator = competition.competitor_code_generator
        if not admin_codegen.code_matches(
                access_code,
                {'admin_privileges': ['create_competitor_codes']}):
            raise PermissionDenied

        class FormClass(forms.Form):
            competitor_privileges = forms.MultipleChoiceField(
                choices=competitor_privilege_choices,
                widget=forms.CheckboxSelectMultiple(),
                required=False, label=_("Competitor privileges"))
            competition_questionset = \
                forms.ModelChoiceField(
                    queryset=CompetitionQuestionSet.objects.filter(
                        competition_id=competition.id),
                    label=_("Competition questionset"))
            code_effects = forms.MultipleChoiceField(
                choices=allowed_effect_choices,
                widget=forms.CheckboxSelectMultiple(),
                required=False, label=_("Code effects"))
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if 'competition_questionset' in data:
                cqs = data['competition_questionset']
                data['competition_questionset'] = [cqs.slug_str()]
            else:
                cqs = None
            c = generator.create_code(data)
            request.profile.created_codes.add(c)
            return redirect('competition_code_list',
                            slug=competition.slug)
    else:
        form = FormClass()
    return render(
        request,
        "bober_simple_competition/competition_code_create.html",
        locals())


# 2.1.2 distribute codes to registered and other users
@login_required
def send_codes(request, slug):
    return render(
        request,
        "bober_simple_competition/send_codes.html", locals())


@smart_competition_admin_code_required
def competition_competitor_code_revoke(request, slug, code_value):
    competition = get_object_or_404(Competition, slug=slug)
    access_code = request.session['access_code']
    admin_codegen = competition.admin_code_generator
    generator = competition.competitor_code_generator
    if not admin_codegen.code_matches(
            access_code,
            {'admin_privileges': ['create_competitor_codes']}):
        raise PermissionDenied
    code = get_object_or_404(request.profile.created_codes, value=code_value, generator=generator)
    code.revoke(timezone.now())


# 2.1.3 view results
# @smart_competition_admin_code_required
# @login_required
@access_code_required
def competition_attempt_list(request, slug, regrade=False):
    competition = Competition.objects.get(slug=slug)
    access_code = request.session['access_code']
    object_list = Attempt.objects.filter(
        competitionquestionset__competition=competition)
    if not competition.administrator_code_generator.code_matches(
            access_code,
            {'admin_privileges': ['view_all_attempts']}):
        if competition.competitor_code_generator.code_matches(
                    access_code,
                    {'competitor_privileges': ['results_before_end']}) \
                or competition.administrator_code_generator.code_matches(
                    access_code,
                    {'competitor_privileges': ['results_before_end']}) \
                or competition.end < timezone.now():
            values = competition.competitor_code_generator.codes.filter(
                creator_set=request.profile).values_list('value', flat=True)
            # print "  values:", values
            object_list = object_list.filter(
                Q(user=request.profile) | Q(access_code__in=values))
        else:
            object_list = object_list.none()
    runtime_manager = None
    for attempt in object_list:
        if runtime_manager is None:
            runtime_manager = graders.RuntimeManager()
        attempt.grade_answers(runtime_manager, regrade)
    return render(
        request,
        "bober_simple_competition/competition_attempt_list.html", locals())


# 2.1.4 mark attempts as invalid
#     all attempts with codes created or distributed by
#     the current user can be accessed
@login_required
def invalidate_attempt(request, slug, attempt_id):
    attempt = Attempt.objects.get(id=attempt_id)
    attempt.invalidated_by = request.profile
    return render(
        request,
        "bober_simple_competition/invalidate_attempt.html", locals())


# 2.1.5 use questionsets
# @login_required
# @access_code_required
@smart_competition_admin_code_required
def use_questionsets(request, slug, competition_questionset_id=None):
    access_code = request.session['access_code']
    competition = Competition.objects.get(slug=slug)
    codegen = competition.administrator_code_generator
    can_use_questionsets = codegen.code_matches(access_code, {
        'admin_privileges': ['use_question_sets']})
    can_use_questions = codegen.code_matches(access_code, {
        'admin_privileges': ['use_questions']})
    if competition_questionset_id is not None:
        cqs = CompetitionQuestionSet.objects.get(id=competition_questionset_id)
        questionsets = [cqs.questionset]
    else:
        questionsets = competition.questionsets.all()
    if request.method == 'POST':
        for qs in questionsets:
            if can_use_questionsets:
                request.profile.question_sets.add(qs)
                for q in qs.questions.all():
                    request.profile.questions.add(q)
        success = True
    else:
        success = False
    return render(
        request,
        "bober_simple_competition/use_questionset.html", locals())


# 2.2 competitor
#     2.2.1 get question page
# @login_required
@access_code_required
def competition_index(request, competition_questionset_id):
    return render(
        request,
        "bober_simple_competition/competition_index.html", locals())


# 2.2.1.1 get question page as guest
def competition_guest(request, competition_questionset_id):
    competition_questionset = get_object_or_404(CompetitionQuestionSet,
                                                id=competition_questionset_id)
    guest_code = competition_questionset.guest_code
    if guest_code is not None:
        code = guest_code.value
        request.session["access_code"] = code
        # print "using code:", code
    else:
        code = None
    # code = ''.join([random.choice(string.digits) for _ in xrange(9)])
    return render(
        request,
        "bober_simple_competition/competition_guest.html", locals())


#   nginx and Apache support access control to static files by an application.
#   Access is granted by setting a header. The name of the header is different
#   for each server and is stored in settings.SAFE_REDIRECT_HEADER.
#   This function sets the correct header.
def safe_media_redirect(resource_path):
    response = HttpResponse()
    response['Content-Type'] = ''
    url = os.path.join(settings.MEDIA_URL, resource_path)
    try:
        response[settings.SAFE_REDIRECT_HEADER] = url
    except Exception:
        response = redirect(url)
    return response


# Helper function - check whether a competitor is accessing their own attempt
# and whether they have the correct access code
def _check_attempt_and_code(request, attempt):
    if attempt.competitor is not None:
        if request.session['competitor_id'] != attempt.competitor_id:
            raise Exception("wrong user")
    if attempt.access_code != request.session['access_code']:
        raise Exception("wrong access code")


# return true if the user is allowed to attempt the competition
def _can_attempt(request, competition_questionset):
    access_allowed = False
    try:
        competition = competition_questionset.competition
        access_code = request.session['access_code']
        now = timezone.now()
        codegen = competition.competitor_code_generator
        access_allowed |= codegen.code_matches(
            access_code, {'competitor_privileges': ['attempt_before_start']})
        access_allowed |= competition.start < now and \
            codegen.code_matches(
                access_code, {'competitor_privileges': ['attempt']})
        access_allowed &= (competition.end > now)
        access_allowed &= codegen.code_matches(
            access_code, {'competition_questionset':
                          [competition_questionset.slug_str()]})
    except Exception as e:
        # TODO: add exception handling
        access_allowed = False
    return access_allowed


# 2.2.2 get question resources for a given questionset
def competition_resources(request, competition_questionset_id, resource_path):
    cq = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id)
    if _can_attempt(request, cq):
        cache_dir = ("caches/" + str(cq.questionset.id) + "-"
                     + cq.questionset.slug)
        return safe_media_redirect(os.path.join(cache_dir, resource_path))
    raise PermissionDenied


@login_required
def question_resources(request, pk, resource_path):
    try:
        q = request.profile.questions.get(pk=pk)
        r = get_object_or_404(Resource, relative_url=resource_path,
                              question_id=pk)
        return HttpResponse(r.data)
    except Exception:
        raise PermissionDenied


# 2.2.3 get question data (existing answers, attempt_id, randomised_question map)
# @login_required
@access_code_required
@ensure_csrf_cookie
def competition_data(request, competition_questionset_id):
    try:
        competitor = Competitor.objects.get(
            id=request.session['competitor_id'])
    except Exception:
        competitor = None
    access_code = request.session['access_code']
    competition_questionset = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id)
    if not _can_attempt(request, competition_questionset):
        try:
            request.session.pop('access_code')
        except Exception:
            pass
        raise PermissionDenied
    try:
        competition = competition_questionset.competition
        codegen = competition.competitor_code_generator
        assert codegen.code_matches(
            access_code, {'competitor_privileges': ['resume_attempt']})
        sep = codegen.format.separator
        # access_code_id_part contains both the group and the code id
        access_code_id_part = sep.join(access_code.split(sep)[:2])
        attempt = Attempt.objects.filter(
            competitor=competitor,
            access_code__startswith=access_code_id_part,
            competitionquestionset_id=competition_questionset_id)[0]
        answers = []
        finish = attempt.finish
        attempt.grade_answers()
        for g_a in attempt.gradedanswer_set():
            val = g_a.answer.value
            if val is None:
                val = ''
            answers.append({'q': a.randomized_question_id, 'a': str(val)})
    except Exception as e:
        competition = competition_questionset.competition
        finish = timezone.now() + datetime.timedelta(
            seconds=competition.duration)
        attempt = Attempt(competitor=competitor,
                          competitionquestionset_id=competition_questionset_id,
                          access_code=access_code,
                          finish=finish,
                          random_seed=random.getrandbits(31))
        attempt.save()
        answers = []
    request.session['attempt_id'] = attempt.id
    data = dict()
    data['attempt_id'] = attempt.id
    data['competition_title'] = competition_questionset.name
    data['question_map'] = attempt.competitionquestionset.questionset.question_mapping(attempt.random_seed)
    data['random_seeds'] = {}
    epoch = datetime.datetime.utcfromtimestamp(0).replace(
        tzinfo=timezone.get_current_timezone())
    data['finish'] = (finish - epoch).total_seconds()
    r = random.Random(attempt.random_seed)
    for i in data['question_map']:
        data['random_seeds'][i] = r.random()
    data['answers'] = answers
    return HttpResponse(json.dumps(data), content_type="application/json")


# 2.2.4 get remaining time
# @login_required
def server_time(request, *args, **kwargs):
    return HttpResponse(json.dumps({'timestamp': time.time()}),
                        content_type="application/json")


def time_remaining(request, competition_questionset_id, attempt_id):
    seconds_left = 0
    try:
        attempt = Attempt.objects.get(id=attempt_id)
        now = timezone.now()
        _check_attempt_and_code(request, attempt)
        seconds_left = (attempt.finish - now).total_seconds()
        if seconds_left < 0:
            all_data = {'success': False, "seconds_to_end": seconds_left,
                        'errorCode': 9}
        else:
            all_data = {'success': True, "seconds_to_end": seconds_left}
    except Exception as e:
        all_data = {'success': False, "seconds_to_end": seconds_left,
                    'message': str(e)}
    return HttpResponse(json.dumps(all_data), content_type="application/json")


# 2.2.5 submit answer
def submit_answer(request, competition_questionset_id, attempt_id):
    data = {}
    try:
        assert request.method == 'POST'
        try:
            val = int(request.POST['a'])
        except Exception:
            val = None
        now = timezone.now()
        remote_addr = request.META.get('REMOTE_ADDR', None)
        a = Answer(attempt_id=attempt_id,
                   randomized_question_id=request.POST['q'],
                   value=val, timestamp=now, remote_addr=remote_addr)
        a.save()
        try:
            # uncomment the line below for offline checking
            raise Exception()

            graded_answer, created = GradedAnswer.objects.get_or_create(
                attempt_id=attempt_id,
                question_id=a.question_id,
                defaults={'answer': a}).select_related('attempt')
            attempt = graded_answer.attempt
            _check_attempt_and_code(request, attempt)
            if (attempt.finish - now).total_seconds() >= 0:
                if not created:
                    graded_answer.answer = a
                    graded_answer.save()
            else:
                if created:
                    graded_answer.delete()
                raise OutOfTimeError("out_of_time")
        except OutOfTimeError as e:
            raise e
        except Exception:
            # TODO: add exception handling
            pass
        data['success'] = True
        # don't do a read before each write!
    except Exception as e:
        data['error'] = True
        data['errorCode'] = str(e)
    return HttpResponse(json.dumps(data), content_type="application/json")


# 2.2.6 finish competition
def finish_competition(request, competition_questionset_id, attempt_id):
    try:
        attempt = Attempt.objects.get(id=attempt_id)
        _check_attempt_and_code(request, attempt)
        attempt.finish = timezone.now()
        attempt.save()
        data = {
            'success': True,
            'redirect_url': reverse('attempt_results', kwargs={
                'competition_questionset_id': competition_questionset_id,
                'attempt_id': attempt_id})
            }
    except Exception as e:
        data = {'success': False, 'error': str(e)}
    return HttpResponse(json.dumps(data), content_type="application/json")


# 2.2.7 view results
# @login_required
@access_code_required
def attempt_results(request, competition_questionset_id, attempt_id):
    attempt = Attempt.objects.get(id=attempt_id)
    competition = attempt.competitionquestionset.competition
    codegen = competition.competitor_code_generator
    access_code = request.session['access_code']
    if codegen.code_matches(
            access_code, {'competitor_privileges': ['results_before_end']}):
        attempt.grade_answers(update_graded=True)
    elif competition.end > timezone.now():
        return redirect('competition_compete', slug=competition.slug)
    object_list = attempt.latest_answers()
    return render(
        request,
        "bober_simple_competition/attempt_results.html", locals())


# 3. create registration codes
def registration_codes(request):
    return render(
        request,
        "bober_simple_competition/registration_codes.html", locals())


# 5. edit user data
# 5.0 list ?users registered using the current user's codes?
# Confirm attempts
@login_required
def attempt_confirm(request, competition_questionset_id, attempt_id):
    if request.method != 'POST':
        raise PermissionDenied
    attempt = get_object_or_404(Attempt, id=attempt_id)
    cqs = get_object_or_404(CompetitionQuestionSet,
                            id=competition_questionset_id)
    profile = request.profile
    if request.profile.created_codes.filter(
                codegenerator=cqs.competition.competitor_code_generator,
                value=attempt.access_code
            ).count() < 1:
        raise PermissionDenied
    ac, created = AttemptConfirmation.objects.get_or_create(
        by=profile,
        attempt=attempt
    )
    return JsonResponse({'id': ac.id, 'status': 'success'})


@login_required
def attempt_unconfirm(request, competition_questionset_id, attempt_id):
    if request.method != 'POST':
        raise PermissionDenied
    attempt = get_object_or_404(Attempt, id=attempt_id)
    cqs = get_object_or_404(CompetitionQuestionSet,
                            id=competition_questionset_id)
    profile = request.profile
    if request.profile.created_codes.filter(
                codegenerator=cqs.competition.competitor_code_generator,
                value=attempt.access_code
            ).count() < 1:
        raise PermissionDenied
    AttemptConfirmation.objects.filter(
        by=profile,
        attempt=attempt
    ).delete()
    return JsonResponse({'status': 'success'})


class CompetitorUpdateJson(LoginRequiredMixin,
                           InvalidFormRespond422, UpdateView):
    model = Competitor
    form_class = CompetitorUpdateForm

    def form_valid(self, form):
        attempt = get_object_or_404(Attempt,
                                    id=form.cleaned_data['attempt_id'])
        if attempt.competitor != self.object:
            raise PermissionDenied
        cqs = get_object_or_404(CompetitionQuestionSet,
                                id=form.cleaned_data['cqs_id'])
        profile = self.request.profile
        if profile.created_codes.filter(
            codegenerator=cqs.competition.competitor_code_generator,
            value=attempt.access_code
        ).count() < 1:
            raise PermissionDenied
        form.save()
        # print "obj:", self.object
        return JsonResponse(
            {
                'status': 'success',
                'first_name': self.object.first_name,
                'last_name': self.object.last_name,
                'date_of_birth': self.object.date_of_birth,
                })


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'bober_simple_competition/profile_list.html'

    def get_context_data(self, **kwargs):
        c = super(ProfileListView, self).get_context_data(**kwargs)
        # print c
        return c

    def get_queryset(self):
        return self.request.profile.managed_profiles.filter(merged_with=None)


class ProfileTableView(LoginRequiredMixin, FilteredSingleTableView):
    table_class = tables.ProfileTable
    filter_class = filters.ProfileFilter
    template_name = 'bober_simple_competition/profile_table_list.html'

    def get_queryset(self):
        return self.request.profile.managed_profiles.filter(merged_with=None)


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile

    def get_queryset(self):
        return self.request.profile.managed_profiles.all()

    def get_object(self, *args, **kwargs):
        obj = super(ProfileDetail, self).get_object(*args, **kwargs)
        while obj.merged_with is not None:
            obj = obj.merged_with
        return obj

# 5.1 merge users
#  any users registered with codes created or distributed
#  by the current user can be merged
# 5.2 edit users
#  the data for users registered with codes created or distributed
#  by the current user can be edited


class ProfileUpdate(LoginRequiredMixin, PopupUpdateView):
    model = Profile
    form_class = ProfileEditForm

    def get_queryset(self):
        return self.request.profile.managed_profiles.all()

    def get_form(self, form_class=ProfileEditForm):
        form = super(PopupUpdateView, self).get_form(form_class)
        if 'merged_with' in form.fields:
            form.fields['merged_with'].queryset = self.get_queryset()
        return form

    def form_valid(self, form):
        if (form.instance.merged_with is not None
                and form.instance.merged_with
                not in self.get_queryset()):
            # print "merged_with user not managed"
            raise PermissionDenied
        return super(ProfileUpdate, self).form_valid(form)

    # def get_success_url(self):
    #   # print self.__dict__
    #   return reverse('profile_detail',
    #        kwargs = {'pk': self.object.id})


class ProfileMerge(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileMergeForm

    def form_valid(self, form):
        if form.instance.merged_with is not None:
            self.merged_pk = form.instance.merged_with_id
        return super(ProfileMerge, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail',
                       kwargs={'pk': self.merged_pk})


class ProfileAutocomplete(autocomplete.Select2QuerySetView):
    model = Profile

    def get_queryset(self):
        profiles = Profile.objects.none()
        if not self.request.user.is_authenticated:
            return profiles
        if self.request.user.is_superuser:
            profiles = Profile.objects.all()
        else:
            profiles = self.request.profile.managed_profiles.all()
        if self.q:
            profiles = profiles.filter(user__username__icontains=self.q)
        return profiles


# 4. register competitor
class QuestionSetCompete(CreateView):
    form_class = QuestionSetCompetitorForm
    template_name = "bober_simple_competition/questionset_registration.html"

    def get_success_url(self):
        return reverse(
            'competition_index',
            kwargs={'competition_questionset_id':
                    self.competitionquestionset.id})

    def dispatch(self, *args, **kwargs):
        cqs = CompetitionQuestionSet.objects.get(
            id=kwargs['competition_questionset_id'])
        self.competitionquestionset = cqs
        self.competition = cqs.competition
        return super(QuestionSetCompete, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionSetCompete, self).get_context_data(**kwargs)
        context['competition'] = self.competition
        context['competitionquestionset'] = self.competitionquestionset
        return context

    def get_initial(self):
        d = super(QuestionSetCompete, self).get_initial()
        if self.request.user.is_authenticated:
            profile = self.request.profile
            d['first_name'] = profile.user.first_name
            d['last_name'] = profile.user.last_name
        d['short_access_code'] = self.request.session.get('short_access_code',
                                                          '')
        return d

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        kwargs = self.get_form_kwargs()
        kwargs['competitionquestionset'] = self.competitionquestionset
        if self.request.user.is_authenticated:
            kwargs['profile'] = self.request.profile
        f = form_class(**kwargs)
        return f

    def form_valid(self, form):
        retval = super(QuestionSetCompete, self).form_valid(form)
        _use_access_code(self.request, form.cleaned_data['full_code'])
        self.request.session['competitor_id'] = form.instance.id
        return retval


class CompetitionCompete(QuestionSetCompete):
    form_class = CompetitionCompetitorForm
    template_name = "bober_simple_competition/competition_registration.html"

    def dispatch(self, *args, **kwargs):
        self.competition = get_object_or_404(Competition, slug=kwargs['slug'])
        self.competitionquestionset = None
        return super(QuestionSetCompete, self).dispatch(*args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        kwargs = self.get_form_kwargs()
        kwargs['competition'] = self.competition
        if self.request.user.is_authenticated:
            kwargs['profile'] = self.request.profile
        f = form_class(**kwargs)
        return f

    def form_valid(self, form):
        self.competitionquestionset = form.cleaned_data['competition_questionset']
        return super(CompetitionCompete, self).form_valid(form)


# 4. register user
class QuestionSetRegistration(CreateView):
    form_class = QuestionSetRegistrationForm
    template_name = "bober_simple_competition/questionset_registration.html"

    def get_success_url(self):
        return reverse(
            'competition_index',
            kwargs={'competition_questionset_id':
                    self.competitionquestionset.id})

    def dispatch(self, *args, **kwargs):
        cqs = CompetitionQuestionSet.objects.get(
            id=kwargs['competition_questionset_id'])
        self.competitionquestionset = cqs
        self.competition = cqs.competition
        return super(QuestionSetRegistration, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionSetRegistration, self).get_context_data(**kwargs)
        context['competition'] = self.competition
        context['competitionquestionset'] = self.competitionquestionset
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if 'access_code' in request.session:
                try:
                    assert _can_attempt(self.request,
                                        self.competitionquestionset)
                except Exception as e:
                    # print "No attempt for you!"
                    request.session.pop('access_code')
                return redirect(self.get_success_url())
            return redirect(
                'competitionquestionset_access_code',
                competition_questionset_id=self.competitionquestionset.id,
                next=self.get_success_url())
        return super(QuestionSetRegistration, self).get(request, *args,
                                                        **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        kwargs['competitionquestionset'] = self.competitionquestionset
        f = form_class(**kwargs)
        return f

    def form_valid(self, form):
        retval = super(QuestionSetRegistration, self).form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
            _use_access_code(self.request, form.cleaned_data['full_code'])
        return retval


class CompetitionRegistration(QuestionSetRegistration):
    form_class = CompetitionRegistrationForm
    template_name = "bober_simple_competition/competition_registration.html"

    def dispatch(self, *args, **kwargs):
        self.competition = Competition.objects.get(slug=kwargs['slug'])
        self.competitionquestionset = None
        return super(QuestionSetRegistration, self).dispatch(*args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        kwargs['competition'] = self.competition
        f = form_class(**kwargs)
        return f

    def get(self, request, *args, **kwargs):
        return super(QuestionSetRegistration, self).get(
            request, *args, **kwargs)

    def form_valid(self, form):
        self.competitionquestionset = form.cleaned_data[
            'competition_questionset']
        return super(CompetitionRegistration, self).form_valid(form)


#   5.3 get certificates, other files
def _profile_file_path(profile, *path):
    return os.path.join('user_files', profile.user.username, *path)


@login_required
def profile_files(request, pk, resource_path):
    profile = request.profile
    if int(pk) not in profile.managed_profiles.all().values_list(
            'id', flat=True):
        raise PermissionDenied
    return safe_media_redirect(_profile_file_path(profile, resource_path))


# 6. import question(s)
class QuestionImport(LoginRequiredMixin, DetailView):
    template_name = "bober_simple_competition/question_import.html"


class QuestionSolution(LoginRequiredMixin, DetailView):
    template_name = "bober_simple_competition/question_solution.html"


class QuestionList(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'bober_simple_competition/question_list.html'

    def get_queryset(self):
        return self.request.profile.questions.all()


class QuestionTableView(LoginRequiredMixin, FilteredSingleTableView):
    table_class = tables.QuestionTable
    filter_class = filters.ProfileFilter
    template_name = 'bober_simple_competition/question_table_list.html'

    def get_queryset(self):
        return self.request.profile.questions.all()


class QuestionDetail(LoginRequiredMixin, DetailView):
    model = Question

    def get_queryset(self):
        return self.request.profile.questions.all()
#
# 7. create questionset from questions


class QuestionSetList(LoginRequiredMixin, ListView):
    model = QuestionSet
    template_name = "questionset_list.html"

    def get_queryset(self):
        return self.request.profile.question_sets.all()


class QuestionSetDetail(LoginRequiredMixin, DetailView):
    model = QuestionSet


class QuestionSetCreate(LoginRequiredMixin, PopupCreateView):
    model = QuestionSet
    form_class = QuestionSetForm

    def form_valid(self, form):
        retval = super(QuestionSetCreate, self).form_valid(form)
        self.request.profile.created_question_sets.add(form.instance)
        self.request.profile.question_sets.add(form.instance)
        return retval

    def get_success_url(self):
        return reverse('questionset_list')


class QuestionSetUpdate(LoginRequiredMixin, PopupUpdateView):
    model = QuestionSet
    form_class = QuestionSetForm

    def get_queryset(self):
        return self.request.profile.created_question_sets.all()

    def get_success_url(self):
        return reverse('questionset_detail',
                       kwargs=self.kwargs)


class QuestionSetDelete(LoginRequiredMixin, DeleteView, PopupFormViewMixin):
    model = QuestionSet

    def get_queryset(self):
        return self.request.profile.created_question_sets.all()
