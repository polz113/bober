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
from django import forms
import code_based_auth.models

import datetime
import json

class CompetitionListView(ListView):
    model = Competition

# Create your views here.
def index(request):
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
def competition_code_create(request, competition_slug, generator='admin'):
    competition = Competition.objects.get(slug=competition_slug)
    if generator == 'admin':
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
                print data ['competition_questionset']
                data['competition_questionset'] = [
                    str(data['competition_questionset'].id) + "-" + \
                        str(data['competition_questionset'].name)
                ]
            print data
            c = generator.create_code(data)
            print c
    else:
        form = FormClass()
    return render(request, 
        "bober_simple_competition/competition_code_create.html",
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
def competition_registration(request, competition_questionset_id):
    if request.method == 'POST':
        form = MinimalCompetitionRegistrationForm(request.POST)
        if form.is_valid():
            request.session['access_code'] = form.cleaned_data['access_code']
            return redirect('competition_index', 
                competition_questionset_id = competition_questionset_id)
    else:
        try:
            form = MinimalCompetitionRegistrationForm(request.GET)
            request.session['access_code'] = form.cleaned_data['access_code']
            return redirect('competition_index', 
                competition_questionset_id = competition_questionset_id)
        except:
            form = MinimalCompetitionRegistrationForm()
    return render(request,
        "bober_simple_competition/competition_registration.html", locals())

#     2.2.1 get question page
@login_required
def competition_index(request, competition_questionset_id):
    return render_to_response("bober_simple_competition/competition_index.html", locals())

# 2.2.2 get question resources
def competition_resources(request, competition_questionset_id, resource_path):
    q = CompetitionQuestionSet.objects.get(
        id=competition_questionset_id).questionset
    cache_dir = "caches/" + str(q.id) + "-" + q.slug
    # TODO change this from a redirect to something more secure
    return redirect('/'.join((settings.MEDIA_URL, cache_dir, resource_path))) 

# 2.2.3 get question data (existing answers, attempt_id, randomised_question map)
@login_required
@ensure_csrf_cookie
def competition_data(request, competition_questionset_id):
    user = request.user
    access_code = request.session['access_code']
    try:
        attempt = Attempt.objects.filter(user=user,
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
    print "finish"
    try:
        attempt = Attempt.objects.get(id=attempt_id)
        attempt.finish = timezone.now()
        attempt.save()
        data = {'success': True}
    except Exception, e:
        data = {'success': False, 'error': str(e)}
    return HttpResponse(json.dumps(data), content_type="application/json")

# 2.2.7 view results
def attempt_results(request, competition_questionset_id, attempt_id):
    pass
    return render_to_response("bober_simple_competition/attempt_results.html", locals())

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
def user_list(request):
    pass
    return render_to_response("bober_simple_competition/user_list.html", locals())

# 5.1 merge users
#  any users registered with codes created or distributed
#  by the current user can be merged
def user_merge(request):
    pass
    return render_to_response("bober_simple_competition/user_merge.html", locals())

# 5.2 edit users
#  the data for users registered with codes created or distributed
#  by the current user can be edited
def user_edit(request):
    pass
    return render_to_response("bober_simple_competition/user_edit.html", locals())

#   5.3 get certificates, other files
def user_files(request):
    pass
    return render_to_response("bober_simple_competition/user_files.html", locals())

# 6. import question(s)
def question_import(request):
    pass
    return render_to_response("bober_simple_competition/question_import.html", locals())

# 7. create questionset from questions
def questionset_create(request):
    pass
    return render_to_response("bober_simple_competition/questionset_create.html", locals())

#   all questions for competitions you have admin access to can be used
# 8. create competition (from multiple questionsets)
#   all questionsets for competitions you have admin access to can be used.
#   Also, newly created questionsets can be used.
def competition_create(request):
    return render_to_response("bober_simple_competition/competition_create.html", locals())

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
