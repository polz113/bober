from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from bober_simple_competition.forms import *
from django.contrib.auth import authenticate, login
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.template import RequestContext
from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django import forms
from django.db.models import Q
from braces.views import LoginRequiredMixin
import code_based_auth.models
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
import datetime
import json
import random
import string

def access_code_required(function = None):
    def code_fn(*args, **kwargs):
        request = kwargs.get('request', args[0])
        try:
            access_code = request.session['access_code']
        except:
            next = request.get_full_path()
            return redirect('access_code', next=next)
        return function(*args, **kwargs)
    return code_fn

class AccessCodeRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AccessCodeRequiredMixin, cls).as_view(**initkwargs)
        return access_code_required(view)

# Create your views here.

def index(request):
#    raise Exception(request.META["SERVER_SOFTWARE"])
    return render_to_response("bober_simple_competition/index.html", locals())

class CompetitionListView(ListView):
    model = Competition

class CompetitionDetailView(DetailView):
    model = Competition

def access_code(request, next):
    qd = QueryDict(dict(), mutable=True)
    qd.update(request.GET)
    qd.update(request.POST)
    form = MinimalAccessCodeForm(qd)
    if form.is_valid():
        request.session['access_code'] = form.cleaned_data['access_code']
        return HttpResponseRedirect(next)
    return render(request, 'bober_simple_competition/access_code.html', locals())

@login_required
def competition_code_list(request, competition_slug):
    competition = Competition.objects.get(slug=competition_slug)
    admin_codegen = competition.administrator_code_generator
    try:
        access_code = request.session['access_code']
    except KeyError:
        access_code = ""
    admin_codes = admin_codegen.codes.all()
    competitor_codes = competition.competitor_code_generator.codes.all()
    if not admin_codegen.code_matches(
            access_code, {'admin_privileges': ['view_all_admin_codes']}):
        admin_codes = admin_codes.filter(
            Q(owner_set=request.user.profile) | Q(user_set=request.user.profile))
    if not admin_codegen.code_matches(
            access_code, {'admin_privileges': ['view_all_competitor_codes']}):
        competitor_codes = competitor_codes.filter(
            Q(owner_set=request.user.profile) | Q(user_set=request.user.profile))
    can_create_administrator_codes = admin_codegen.code_matches(
        access_code, {'admin_privileges': ['create_admin_codes']})
    can_create_competitor_codes = admin_codegen.code_matches(
        access_code, {'admin_privileges': ['create_competitor_codes']})
    return render_to_response("bober_simple_competition/competition_code_list.html", locals())

# codes can have the following permissions:
# 1. can create admin codes for this competition
# 2. can create teacher codes for this competition
# 3. can create student codes for this competition
# 4. can attempt competition
# 5. can attempt competition before official start
# 6. can view results before official end
# 7. can use questionset to create new competitions
@login_required
@access_code_required
def competition_code_create(request, competition_slug, user_type='admin'):
    access_code = request.session['access_code']
    competition = Competition.objects.get(slug=competition_slug)
    admin_codegen = competition.administrator_code_generator
    competitor_privilege_choices = filter(
        lambda x: admin_codegen.code_matches(access_code,
            {'competitor_privileges': [x[0]]}),
        COMPETITOR_PRIVILEGES)
    admin_privilege_choices = list()
    if user_type == 'admin':
        if not admin_codegen.code_matches(access_code,
                {'admin_privileges': ['create_admin_codes']}):
            raise PermissionDenied;
        admin_privilege_choices = filter(
            lambda x: admin_codegen.code_matches(access_code,
                {'admin_privileges': [x[0]]}),
            ADMIN_PRIVILEGES)
        generator = admin_codegen
        class FormClass(forms.Form):
            competitor_privileges = forms.MultipleChoiceField(
                choices = competitor_privilege_choices, required = False)
            admin_privileges = forms.MultipleChoiceField(
                choices = admin_privilege_choices, required = False)
            code_effects = forms.MultipleChoiceField(
                choices = CODE_EFFECTS, required = False)
    else:
        generator = competition.competitor_code_generator
        if not admin_codegen.code_matches(access_code, 
                {'admin_privileges': ['create_competitor_codes']}):
            raise PermissionDenied;
        class FormClass(forms.Form):
            competitor_privileges = forms.MultipleChoiceField(
                choices = competitor_privilege_choices, required = False)
            competition_questionset = \
                forms.ModelChoiceField(
                    queryset=CompetitionQuestionSet.objects.filter(
                        competition_id=competition.id))
            code_effects = forms.MultipleChoiceField(
                choices = CODE_EFFECTS, required = False)
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if 'competition_questionset' in data:
                data['competition_questionset'] = [
                    str(data['competition_questionset'].id) + "." + \
                        str(data['competition_questionset'].name)
                ]
            c = generator.create_code(data)
            request.user.profile.created_codes.add(c)
            return redirect('competition_code_list',
                competition_slug = competition.slug)
    else:
        form = FormClass()
    return render(request, 
        "bober_simple_competition/competition_code_create.html",
        locals())

@login_required
def code_format_create(request, user_type='admin'):
    created = False
    if user_type == 'admin':
        FormClass = AdminCodeFormatForm
    else:
        FormClass = CompetitorCodeFormatForm
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            code_components = [
                {
                    'name': 'code_id',
                    'hash_bits': form.cleaned_data['code_id_bits'],
                    'hash_format': 'a',
                    'hash_algorithm': 'noop',
                    'max_parts': 1,
                },
                {
                    'name': 'code_effects',
                    'hash_bits': form.cleaned_data['code_effects_bits'],
                    'hash_format': form.cleaned_data['code_effects_format'],
                    'hash_algorithm': form.cleaned_data['code_effects_hash'],
                    'max_parts': len(CODE_EFFECTS),
                },
                {
                    'name': 'competitor_privileges',
                    'hash_bits': form.cleaned_data['competitor_privilege_bits'],
                    'hash_format': form.cleaned_data['competitor_privilege_format'],
                    'hash_algorithm': form.cleaned_data['competitor_privilege_hash'],
                    'max_parts': len(COMPETITOR_PRIVILEGES),
                }]
            if user_type == 'admin':
                code_components += [{
                    'name': 'admin_privileges',
                    'hash_bits': form.cleaned_data['admin_privilege_bits'],
                    'hash_format': form.cleaned_data['admin_privilege_format'],
                    'hash_algorithm': form.cleaned_data['admin_privilege_hash'],
                    'max_parts': len(ADMIN_PRIVILEGES),
                }]
            else:
                code_components += [{
                    'name': 'competition_questionset',
                    'hash_bits': form.cleaned_data['questionset_bits'],
                    'hash_format': form.cleaned_data['questionset_format'],
                    'hash_algorithm': form.cleaned_data['questionset_hash'],
                    'max_parts': 1,
                }]
            f = code_based_auth.models.CodeFormat.from_components(code_components)
            created = True
    else:
        form = FormClass()
    return render(request, 
        "bober_simple_competition/code_format_create.html",
        locals())

# 2.1.2 distribute codes to registered and other users
@login_required
def send_codes(request, competition_slug):
    return render(request, "bober_simple_competition/send_codes.html", locals())

# 2.1.3 view results
@login_required
@access_code_required
def competition_attempt_list(request, competition_slug):
    competition = Competition.objects.get(slug=competition_slug)
    access_code = request.session['access_code']
    object_list = Attempt.objects.filter(
        competitionquestionset__competition = competition)
    if not competition.administrator_code_generator.code_matches(access_code,
            {'admin_privileges': ['view_all_attempts']}):
        print "filtering", access_code
        if competition.competitor_code_generator.code_matches(access_code,
                    {'competitor_privileges': ['results_before_end']}) \
                or competition.administrator_code_generator.code_matches(access_code,
                    {'competitor_privileges': ['results_before_end']}) \
                or competition.end < timezone.now():
            values = competition.competitor_code_generator.codes.filter(
                owner_set = request.user.profile).values_list('value', flat=True)
            print "  values:", values
            object_list = object_list.filter(
                Q(user=request.user.profile) | Q(access_code__in=values))
        else:
            object_list = object_list.none()
    return render(request, 
        "bober_simple_competition/competition_attempt_list.html", locals())

# 2.1.4 mark attempts as invalid
#     all attempts with codes created or distributed by
#     the current user can be accessed 
@login_required
def invalidate_attempt(request, competition_slug, attempt_id):
    attempt = Attempt.objects.get(id=attempt.id)
    attempt.invalidated_by = request.user.profile
    return render_to_response("bober_simple_competition/invalidate_attempt.html", locals())

# 2.2 competitor
#     2.2.1 get question page
# @login_required
# @access_code_required
class CompetitionRegistration(FormView):
    pass

def competition_registration(request, competition_questionset_id):
    if request.user.is_authenticated():
        return redirect('competition_index',
            competition_questionset_id = competition_questionset_id)
    if request.method == "POST":
        competition = CompetitionQuestionSet.objects.get(
            id=competition_questionset_id).competition
        d = QueryDict(dict(), mutable=True)
        d.update(request.POST)
        d['competition'] = competition.id
        form = CompetitionRegistrationForm(d)
        if form.is_valid():
            # print form.cleaned_data
            profile = form.save()
            u = authenticate(username=profile.user.username,
                password=form.cleaned_data['password'])
            login(request, u)
            request.session['access_code'] = form.cleaned_data[
                'access_code']
            return redirect('competition_index',
                competition_questionset_id = competition_questionset_id)
    else:
        if request.GET.get('register_as', None) == 'admin':
            register_as = 'admin'
        else:
            register_as = 'competitor'
        initial = {'register_as': register_as}
        form = CompetitionRegistrationForm(initial = initial)
    return render(request, 
        "bober_simple_competition/competition_registration.html",
        locals())


    form = CompetitionRegistrationForm()
#     2.2.1 get question page
# @login_required
@access_code_required
def competition_index(request, competition_questionset_id):
    return render_to_response("bober_simple_competition/competition_index.html", locals())

#	2.2.1.1 get question page as guest
def competition_guest(request, competition_questionset_id):
    competition_questionset = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id)
    guest_code = competition_questionset.competition.guest_code
    if guest_code is not None:
        code = guest_access_code.value
        request.session["access_code"] = code
    else:
        code = None
	# code = ''.join([random.choice(string.digits) for _ in xrange(9)])
	return render_to_response("bober_simple_competition/competition_guest.html", locals())

#   nginx and Apache support access control to static files by an application.
#   Access is granted by setting a header. The name of the header is different
#   for each server and is stored in settings.SAFE_REDIRECT_HEADER.
#   This function sets the correct header.
def safe_media_redirect(resource_path):
    response = HttpResponse()
    response['Content-Type'] = ''
    url = (os.path.join(settings.MEDIA_URL, resource_path)).encode('utf-8')
    try:
        response[settings.SAFE_REDIRECT_HEADER] = url
    except:
        response = redirect(url)
    return response

# Helper function - check whether a competitor is accessing their own attempt
# and whether they have the correct access code
def _check_attempt_and_code(request, attempt):
    if attempt.user is not None:
        if request.user.profile != attempt.user:
            raise Exception("wrong user")
    if attempt.access_code != request.session['access_code']:
        raise Exception("wrong access code")

# return true if the user is allowed to attempt the competition
def _can_attempt(request, competition_questionset):
    access_allowed = False
    try:
        competition = competition_questionset.competition
        access_code = request.session['access_code']
        codegen = competition.competitor_code_generator
        access_allowed |= codegen.code_matches(
            access_code, {'competitor_privileges':['attempt_before_start']})
        access_allowed |= competition.start < timezone.now() and \
            codegen.code_matches(
                access_code, {'competitor_privileges':['attempt']})
        guest_code = competition.guest_code
        access_allowed |= guest_code.value == access_code
    except Exception, e:
        pass
    return access_allowed

# 2.2.2 get question resources for a given questionset
def competition_resources(request, competition_questionset_id, resource_path):
    cq = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id)
    if _can_attempt(request, cq):
        cache_dir = "caches/" + str(cq.questionset.id) + "-" + cq.questionset.slug
        return safe_media_redirect(os.path.join(cache_dir, resource_path))
    raise PermissionDenied 



# 2.2.3 get question data (existing answers, attempt_id, randomised_question map)
# @login_required
@access_code_required
@ensure_csrf_cookie
def competition_data(request, competition_questionset_id):
    try:
        user_profile = request.user.profile
    except:
        user_profile = None
    access_code = request.session['access_code']
    competition_questionset = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id)
    if not _can_attempt(request, competition_questionset):
        raise PermissionDenied
    try:
        attempt = Attempt.objects.filter(user=user_profile,
            access_code=access_code,
            competitionquestionset_id = competition_questionset_id)[0]
        answers = []
        for a in attempt.latest_answers():
            val = a.value
            if val is None:
                val = ''
            answers.append({ 'q': a.randomized_question_id, 'a': str(val)})
    except Exception, e:
        finish = timezone.now() + datetime.timedelta(
            seconds = competition_questionset.competition.duration)
        attempt = Attempt(user=user_profile,
            competitionquestionset_id = competition_questionset_id,
            access_code=access_code,
            finish = finish,
            random_seed = random.getrandbits(31))
        attempt.save()
        answers = []
    request.session['attempt_id'] = attempt.id
    data = dict()
    data['attempt_id'] = attempt.id
    data['competition_title'] = competition_questionset.questionset.name
    data['question_map'] = attempt.competitionquestionset.questionset.question_mapping(attempt.random_seed)
    data['random_seeds'] = {}
    r = random.Random(attempt.random_seed)
    for i in data['question_map']:
        data['random_seeds'][i] = r.random()
    data['answers'] = answers
    return HttpResponse(json.dumps(data), content_type="application/json")

# 2.2.4 get remaining time
# @login_required
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
    except Exception, e:
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
        except:
            val = None
        attempt = Attempt.objects.get(id=attempt_id)
        _check_attempt_and_code(request, attempt)
        now = timezone.now()
        if (attempt.finish - now).total_seconds() < 0:
             raise Exception("out of time")
        a = Answer(attempt_id = attempt_id,
            randomized_question_id = request.POST['q'],
            value = val, timestamp = now)
        a.save()
        data['success'] = True
        # don't do a read before each write!
    except Exception, e:
        data['error'] = True
        data['errorCode'] = str(e);
    return HttpResponse(json.dumps(data), content_type="application/json")

# 2.2.6 finish competition
def finish_competition(request, competition_questionset_id, attempt_id):
    try:
        attempt = Attempt.objects.get(id=attempt_id)
        _check_attempt_and_code(request, attempt)
        attempt.finish = timezone.now()
        attempt.save()
        data = {'success': True, 
            'redirect_url': reverse('attempt_results', kwargs = {
                'competition_questionset_id': competition_questionset_id,
                'attempt_id': attempt_id})
            }
    except Exception, e:
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
    if not (competition.end < timezone.now() or codegen.code_matches(
        access_code, {'competitor_privileges':['results_before_end']})):
        raise PermissionDenied
    object_list = attempt.latest_answers()
    return render(request, "bober_simple_competition/attempt_results.html", locals())

# 3. create registration codes
def registration_codes(request):
    pass
    return render_to_response("bober_simple_competition/registration_codes.html", locals())

# 4. register as user
def user_registration(request):
    if request.method == "POST":
        registration_form = CodeRegistrationForm(request.POST)
        if registration_form.is_valid():
            profile = registration_form.save()
            return render(request, "bober_simple_competition/user_registration_confirmation.html", locals())
    else:
        registration_form = CodeRegistrationForm()
    return render(request, "bober_simple_competition/user_registration.html",
        locals())

# 5. edit user data
# 5.0 list ?users registered using the current user's codes?
class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'bober_simple_competition/profile_list.html'
    def get_context_data(self, **kwargs):
        c = super(ProfileListView, self).get_context_data(**kwargs)
        print c
        return c
    def get_queryset(self):
        return self.request.user.profile.managed_users.all() 

class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
    def get(self, request):
        try:
            f = self.request.user.profile.managed_users.get(id=self.object.id)
        except:
            return PermissionDenied
        return super(ProfileDetail, self).get(request)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile_list')
    def form_valid(self, form):
        try:
            f = self.request.user.profile.managed_users.get(id=form.instance.id)
        except:
            return PermissionDenied
        return super(ProfileUpdate, self).form_valid(form)

@login_required
def user_list(request, competition_id = None):
    object_list = request.user.profile.managed_users.all()
    return render_to_response("bober_simple_competition/user_list.html", locals())

# 5.1 merge users
#  any users registered with codes created or distributed
#  by the current user can be merged
@login_required
def user_merge(request):
    pass
    return render_to_response("bober_simple_competition/user_merge.html", locals())

# 5.2 edit users
#  the data for users registered with codes created or distributed
#  by the current user can be edited
@login_required
def user_edit(request, user_id):
    
    return render_to_response("bober_simple_competition/user_edit.html", locals())

#   5.3 get certificates, other files
@login_required
def user_files(request):
    pass
    return render_to_response("bober_simple_competition/user_files.html", locals())

# 6. import question(s)
@login_required
def question_import(request):
    pass
    return render_to_response("bober_simple_competition/question_import.html", locals())

# 7. create questionset from questions
@login_required
def questionset_create(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render_to_response("bober_simple_competition/questionset_create.html", locals())

#   all questions for competitions you have admin access to can be used
# 8. create competition (from multiple questionsets)
#   all questionsets for competitions you have admin access to can be used.
#   Also, newly created questionsets can be used.
@login_required
def competition_create(request):
    formset = CompetitionFormSet()
    if request.method == 'POST':
        form = CompetitionCreateForm(request.POST)
        if form.is_valid():
            admin_codegen = code_based_auth.models.CodeGenerator(
                unique_code_component = 'code_id',
                format = form.cleaned_data['admin_code_format'],
                salt = form.cleaned_data['admin_salt'])
            admin_codegen.save()
            competitor_codegen = code_based_auth.models.CodeGenerator(
                unique_code_component = 'code_id',
                format = form.cleaned_data['competitor_code_format'],
                salt = form.cleaned_data['competitor_salt'])
            competitor_codegen.save()
            competition = form.instance
            competition.administrator_code_generator = admin_codegen
            competition.competitor_code_generator = competitor_codegen
            competition.save()
            master_code = competition.administrator_code_generator.create_code({
                'admin_privileges': [i[0] for i in ADMIN_PRIVILEGES],
                'competitor_privileges': [i[0] for i in COMPETITOR_PRIVILEGES],
                'code_effects': [i[0] for i in CODE_EFFECTS]
            })
            master_code.save()
            request.user.profile.received_codes.add(master_code)
    else:
        form = CompetitionCreateForm(initial={
            'admin_code_format':
                (code_based_auth.models.CodeFormat.objects.filter(
                    components__name = 'admin_privileges'
                ).order_by('id')[:1] or [None])[0],
            'competitor_code_format':
                (code_based_auth.models.CodeFormat.objects.filter(
                    components__name = 'competition_questionset'
                ).order_by('id')[:1] or [None])[0],
            'admin_salt': ''.join([
                random.choice(string.letters+string.digits) 
                for i in xrange(10)]),
            'competitor_salt': ''.join([
                random.choice(string.letters+string.digits) 
                for i in xrange(10)]),
            })
    return render(request, "bober_simple_competition/competition_create.html", locals())

# shortcut for registering and competing immediately 
def immediate_competition(request):
    # register competitor
    if request.method == 'POST':
        form = ImmediateCompetitionForm(request.POST)
        if form.is_valid():
            request.session['access_code'] = form.cleaned_data['registration_code']
            return redirect('competition_index', 
                competition_questionset_id = competition_questionset_id)
    else:
        form = ImmediateCompetitionForm()
    return render(request,
        "bober_simple_competition/immediate_competition.html", locals())
