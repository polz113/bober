from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from bober_competition.forms import JuniorResult
import bober_competition.models

# Create your views here.

@login_required
def school_mentor(request):
    user = bober_competition.models.Users.objects.get(username=request.user.username)
    seznam = user.competition_category_school_mentor_set.all()
    #seznam = bober_competition.models.SchoolMentor.objects.all()
    return render_to_response("bober_competition/school_mentor.html", locals())

def junior_results(request):
    form = JuniorResult
    return render_to_response("bober_competition/junior_results.html", locals())