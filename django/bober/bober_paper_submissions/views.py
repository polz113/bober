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
from bober_paper_submissions.models import JuniorYear, JuniorMentorship, Competition, JuniorAttempt, JuniorAward
import bober_paper_submissions.models
from bober_simple_competition.views import safe_media_redirect, user_files, _user_file_path
from bober_si.views import AWARD_TEMPLATE_DIR
from bober_si.award_gen import generate_award_pdf
import os

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
    def get_success_url(self):
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
    
@login_required
def junior_award_pdf(request, slug, school_id, year_name):
    profile = request.user.profile
    cert_dir = os.path.join(_user_file_path(profile, school_id))
    cert_fname = year_name + '.pdf'
    cert_path = os.path.join(cert_dir, cert_fname)
    cert_full_fname = os.path.join(settings.MEDIA_ROOT, cert_path)
    try:
        assert os.path.isfile(cert_full_fname)
    except:
        try:
            cert_full_dir = os.path.join(settings.MEDIA_ROOT, cert_dir)
            os.makedirs(cert_full_dir)
        except Exception, e:
            pass
            print e
        # regenerate award. Ignore the template
        template_file = os.path.join(AWARD_TEMPLATE_DIR, 'all_si.svg')
        #print "generating..."
        data = list()
        competition = SchoolCompetition.get_cached_by_slug(slug=slug)
        for junior_year in JuniorYear.objects.filter(
                mentorship__competition = competition,
                mentorship__teacher = profile).select_related(
                'mentorship', 'mentorship__school').distinct():
            school = junior_year.mentorship.school
            #print "    ", school, cqs
            #CompetitionQuestionSet.objects.get(competition=competition,
            #    name = cqs_name)
            junior_attempts = JuniorAttempt.objects.filter(
                    year_class = junior_year
                ).select_related(
                    'competitor',
                ).prefetch_related(
                    'junioraward_set',
                )
            for attempt in junior_attempts:
                for award in attempt.junioraward_set.all().select_related('award'):
                    data.append(
                        {
                            'name': u" ".join((attempt.competitor.first_name, attempt.competitor.last_name)),
                            'school': school.name,
                            'group': junior_year.name,
                            'serial': award.serial,
                            'template': award.award.template,
                        }
                    )
        #    print data
        #print os.path.join(cert_full_dir, cert_fname)
        generate_award_pdf(cert_full_fname,
            data, template_file)
    pass
    #return None
    return safe_media_redirect(cert_path)


