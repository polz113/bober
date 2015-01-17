from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from bober_simple_competition.forms import *
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from django.template import RequestContext
from django.views.generic import ListView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django import forms
import code_based_auth.models
from django.core.urlresolvers import reverse
import datetime
import json
import random
import string

class CompetitionListView(ListView):
    model = Competition

# Create your views here.
def index(request):
#    raise Exception(request.META["SERVER_SOFTWARE"])
    return render_to_response("bober_simple_competition/index.html", locals())

@login_required
def competition_code_list(request, competition_slug):
    competition = Competition.objects.get(slug=competition_slug)
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
def competition_code_create(request, competition_slug, user_type='admin'):
    competition = Competition.objects.get(slug=competition_slug)
    if user_type == 'admin':
        generator = competition.administrator_code_generator
        class FormClass(forms.Form):
            competitor_privileges = forms.MultipleChoiceField(
                choices = COMPETITOR_PRIVILEGES, required = False)
            admin_privileges = forms.MultipleChoiceField(
                choices = ADMIN_PRIVILEGES, required = False)
    else:
        generator = competition.competitor_code_generator
        class FormClass(forms.Form):
            competitor_privileges = forms.MultipleChoiceField(
                choices = COMPETITOR_PRIVILEGES, required = False)
            competition_questionset = \
                forms.ModelChoiceField(
                    queryset=CompetitionQuestionSet.objects.filter(
                        competition_id=competition.id))
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
    else:
        form = FormClass()
    return render(request, 
        "bober_simple_competition/competition_code_create.html",
        locals())

@login_required
def code_format_create(request, user_type='admin'):
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
def competition_attempt_list(request, competition_slug):
    object_list = Attempt.objects.filter(
        competitionquestionset__competition__slug = competition_slug)
    return render(request, 
        "bober_simple_competition/competition_attempt_list.html", locals())

# 2.1.4 mark attempts as invalid
#     all attempts with codes created or distributed by
#     the current user can be accessed 
def disqualify_attempt(request, competition_slug, attempt_id):
    pass
    return render_to_response("bober_simple_competition/disqualify_attempt.html", locals())

# 2.2 competitor
#     2.2.1 get question page
@login_required
def competition_registration(request, competition_questionset_id, access_code=None):
    if request.method == 'POST':
        form = MinimalCompetitionRegistrationForm(request.POST)
        if form.is_valid():
            request.session['access_code'] = form.cleaned_data['access_code']
            return redirect('competition_index', 
                competition_questionset_id = competition_questionset_id)
    else:
        try:
            form = MinimalCompetitionRegistrationForm(request.GET)
            if not form.is_valid():
                raise "form invalid"
            request.session['access_code'] = form.cleaned_data['access_code']
            return redirect('competition_index', 
                competition_questionset_id = competition_questionset_id)
        except Exception, e:
            print e
            form = MinimalCompetitionRegistrationForm()
    return render(request,
        "bober_simple_competition/competition_registration.html", locals())        

#     2.2.1 get question page
@login_required
def competition_index(request, competition_questionset_id):
    return render_to_response("bober_simple_competition/competition_index.html", locals())

#	2.2.1.1 get question page as guest
def competition_guest(request, competition_questionset_id):
	code = ''.join([random.choice(string.digits) for _ in xrange(9)])
	return render_to_response("bober_simple_competition/competition_guest.html", locals())
	
def safe_media_redirect(resource_path):
    response = HttpResponse()
    response['Content-Type'] = ''
    url = (os.path.join(settings.MEDIA_URL, resource_path)).encode('utf-8')
    try:
        response[settings.SAFE_REDIRECT_HEADER] = url
    except:
        response = redirect(url)
    return response

# 2.2.2 get question resources
def competition_resources(request, competition_questionset_id, resource_path):
    q = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id).questionset
    cache_dir = "caches/" + str(q.id) + "-" + q.slug
    return safe_media_redirect(os.path.join(cache_dir, resource_path)) 

# 2.2.3 get question data (existing answers, attempt_id, randomised_question map)
@login_required
@ensure_csrf_cookie
def competition_data(request, competition_questionset_id):
    user = request.user
    access_code = request.session['access_code']
    try:
        attempt = Attempt.objects.filter(user=user.profile,
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
            seconds = CompetitionQuestionSet.objects.get(
                id=competition_questionset_id).competition.duration)
        attempt = Attempt(user=user.profile,
            competitionquestionset_id = competition_questionset_id,
            access_code=access_code,
            finish = finish,
            random_seed = random.getrandbits(31))
        attempt.save()
        answers = []
    request.session.attempt_id = attempt.id
    request.session.access_code = attempt.access_code
    data = dict()
    data['attempt_id'] = attempt.id
    data['question_map'] = attempt.competitionquestionset.questionset.question_mapping(attempt.random_seed)
    data['random_seeds'] = {}
    r = random.Random(attempt.random_seed)
    for i in data['question_map']:
        data['random_seeds'][i] = r.random()
    data['answers'] = answers
    return HttpResponse(json.dumps(data), content_type="application/json")

# 2.2.4 get remaining time
@login_required
def time_remaining(request, competition_questionset_id, attempt_id):
    attempt = Attempt.objects.get(id=attempt_id)
    now = timezone.now()
    try:
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
        a = Answer(attempt_id = attempt_id,
            randomized_question_id = request.POST['q'],
            value = val)
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
@login_required
def attempt_results(request, competition_questionset_id, attempt_id):
    attempt = Attempt.objects.get(id=attempt_id)
    object_list = attempt.latest_answers()
    return render(request, "bober_simple_competition/attempt_results.html", locals())

# 3. create registration codes
def registration_codes(request):
    pass
    return render_to_response("bober_simple_competition/registration_codes.html", locals())

# 4. register as user
def user_registration(request):
    if request.method == "POST":
        registration_form = VCardRegistrationForm(request.POST)
    else:
        registration_form = VCardRegistrationForm()
    return render_to_response("bober_simple_competition/user_registration.html", locals())

# 5. edit user data
@login_required
def user_list(request):
    pass
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
def user_edit(request):
    pass
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
                'competitor_privileges': [i[0] for i in COMPETITOR_PRIVILEGES]
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
