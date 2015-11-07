#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from bober_paper_submissions.forms import JuniorYearForm, JuniorMentorshipForm, JuniorYearInline
from bober_si.models import School, SchoolTeacherCode
from bober_paper_submissions.models import JuniorYear, JuniorMentorship, Competition
import bober_paper_submissions.models

# Create your views here.

@login_required
def mentorship_list(request, slug):
    profile = request.user.profile
    competition = Competition.objects.get(slug=slug)
    #mentorship_list = JuniorMentorship.objects.filter(
    #    competition=competition, teacher = profile)
    mentorship_list = list()
    for school_id in SchoolTeacherCode.objects.filter(
            teacher = profile,
            code__codegenerator = competition.competitor_code_generator,
        ).values_list('school_id', flat=True).distinct():
        mentorship, created = JuniorMentorship.objects.get_or_create(
            competition = competition,
            teacher = profile,
            school_id = school_id)
        mentorship.save()
        mentorship_list.append(mentorship)
    if len(mentorship_list) == 1:
        return redirect('junior_results', pk = mentorship_list[0].id)
    #seznam = bober_competition.models.SchoolMentor.objects.all()
    return render(request, "bober_paper_submissions/school_mentor.html",
        {'object_list': mentorship_list, 'slug':slug})

class JuniorResults(UpdateWithInlinesView, LoginRequiredMixin):
    model = JuniorMentorship
    form_class = JuniorMentorshipForm
    inlines = [JuniorYearInline,]
    template_name = "bober_paper_submissions/junior_results.html"
    def dispatch(self, *args, **kwargs):
        self.competition_slug = kwargs.get('slug', None)
        return super(JuniorResults, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        print self.competition_slug
        return reverse('teacher_overview', kwargs={'slug': self.competition_slug})

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
    
