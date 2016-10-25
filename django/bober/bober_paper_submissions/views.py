#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from bober_paper_submissions.forms import JuniorYearForm, JuniorMentorshipForm, JuniorYearInline
from bober_si.models import School, SchoolTeacherCode, SchoolCompetition
from bober_paper_submissions.models import JuniorYear, JuniorMentorship, Competition, JuniorAttempt
import bober_paper_submissions.models
from bober_simple_competition.views import safe_media_redirect
from bober_si.views import AWARD_TEMPLATE_DIR
from bober_si.award_gen import generate_award_pdf
import os

# Create your views here.

@login_required
def mentorship_list(request, slug):
    profile = request.profile
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
        if created:
            mentorship.save()
        mentorship_list.append(mentorship)
    if len(mentorship_list) == 1:
        return redirect('junior_results', slug=slug, pk = mentorship_list[0].id)
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

    def forms_valid(self, form, inlines):
        for inline_set in inlines:
            for inline in inline_set:
                inline.instance.save_results(
                    inline.competitor_data, self.request.profile)
        return super(JuniorResults, self).forms_valid(form, inlines)

    def get_success_url(self):
        return reverse('teacher_overview', kwargs={'slug': self.competition_slug})

