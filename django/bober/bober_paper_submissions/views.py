from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from bober_paper_submissions.forms import JuniorResult
import bober_competition.models
import bober_paper_submissions.models

# Create your views here.

@login_required
def school_mentor(request):
    user = bober_competition.models.Users.objects.get(username=request.user.username)
    seznam = user.competition_category_school_mentor_set.all()
    #seznam = bober_competition.models.SchoolMentor.objects.all()
    return render_to_response("bober_paper_submissions/school_mentor.html", locals())

def junior_results(request, competition_category_school_mentor_id):
    obj, created = bober_paper_submissions.models.JuniorResult.objects.get_or_create(school_mentor_id = int(competition_category_school_mentor_id))
    if request.method == 'POST':
        first_visit = False
        form = JuniorResult(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        first_visit = created
        form = JuniorResult(instance = obj)
    return render(request, "bober_paper_submissions/junior_results.html", locals())
