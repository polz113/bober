#!/usr/bin/python
# -*- coding: utf8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from bober_paper_submissions.forms import JuniorResultForm
import bober_competition.models
import bober_paper_submissions.models

# Create your views here.

@login_required
def school_mentor(request):
    user = bober_competition.models.Users.objects.get(username=request.user.username)
    seznam = user.competition_category_school_mentor_set.all()
    if len(seznam) == 1:
        return redirect('junior_results', competition_category_school_mentor_id = seznam[0].id)
    #seznam = bober_competition.models.SchoolMentor.objects.all()
    return render_to_response("bober_paper_submissions/school_mentor.html", locals())

def junior_results(request, competition_category_school_mentor_id):
    obj, created = bober_paper_submissions.models.JuniorResult.objects.get_or_create(school_mentor_id = int(competition_category_school_mentor_id))
    if request.method == 'POST':
        first_visit = False
        form = JuniorResultForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        first_visit = created
        if first_visit:
            obj.drugi_razred = u"Jože Primer  10\nJana Novak 11\nTina Pobriši T. Primere 8\n"
            obj.save()
        form = JuniorResultForm(instance = obj)
    return render(request, "bober_paper_submissions/junior_results.html", locals())
