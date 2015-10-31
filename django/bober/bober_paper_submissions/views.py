#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from bober_paper_submissions.forms import JuniorResultForm
import bober_si.models
import bober_paper_submissions.models

# Create your views here.

@login_required
def school_mentor(request):
    
    if len(seznam) == 1:
        return redirect('junior_results', competition_category_school_mentor_id = seznam[0].id)
    #seznam = bober_competition.models.SchoolMentor.objects.all()
    return render_to_response("bober_paper_submissions/school_mentor.html", locals())

@login_required
def junior_results(request, competition_category_school_mentor_id):
    obj, created = bober_paper_submissions.models.JuniorResult.objects.get_or_create(school_mentor_id = int(competition_category_school_mentor_id))
    data_saved = False
    form_data_error = False
    if request.method == 'POST':
        first_visit = False
        form = JuniorResultForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            data_saved = True
        else:
            form_data_error = True
    else:
        first_visit = created
        if first_visit:
            obj.drugi_razred = u"Jože Primer  10\nJana Novak 11\nTina Pobriši T. Primere 8\n"
            obj.save()
        form = JuniorResultForm(instance = obj)
    return render(request, "bober_paper_submissions/junior_results.html", locals())

@login_required
def competition_category_results_by_school(request, competition_category_id):
    c = bober_competition.models.CompetitionCategory.objects.get(id=int(competition_category_id))
    d = {}
    for ccs in c.competitioncategoryschool_set.all():
        competition_key = (ccs.competition.id, ccs.competition.name)
        competition_data = d.get(competition_key, {})
        school_key = ccs.school.name
        school_data = competition_data.get(school_key, {})
        for ccsm in ccs.competitioncategoryschoolmentor_set.all():
            mentor_key = ccsm.user.email
            mentor_data = {'drugi_razred': [], 'tretji_razred':[], 'cetrti_razred': [], 'peti_razred':[]}
            for jr in ccsm.juniorresult_set.all():
                mentor_data['drugi_razred'].append(jr.drugi_razred)
                mentor_data['tretji_razred'].append(jr.tretji_razred)
                mentor_data['cetrti_razred'].append(jr.cetrti_razred)
                mentor_data['peti_razred'].append(jr.peti_razred)
            school_data[mentor_key] = mentor_data
        competition_data[school_key] = school_data
        d[competition_key] = competition_data
    return HttpResponse(cPickle.dumps(d), content_type='application/python-pickle')
    
