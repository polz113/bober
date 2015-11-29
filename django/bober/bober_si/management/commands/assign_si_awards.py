#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Assign awards according to slovenian rules"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs='+')

    def __create_awards(self, cqs, group_name, all_attempts, max_score):
        year_str = str(timezone.now().year)[-2:]
        print "creating for", cqs
        group_prefix = {
            '1. letnik': '11',
            '2. letnik': '12',
            '3. letnik': '13',
            '4. letnik': '14',
            '1. razred': '01',
            '2. razred': '02',
            '3. razred': '03',
            '4. razred': '04',
            '5. razred': '05',
            '6. razred': '06',
            '7. razred': '07',
            '8. razred': '08',
            '9. razred': '09',
        }.get(group_name, group_name[:2])
        bronze_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            template = 'bronasto',
            name = 'bronasto',
            defaults = {
                'threshold': max_score,
                'serial_prefix': year_str + group_prefix,
            }
        )
        if created:
            l = []
            for a in all_attempts:
                l.append(a.score)
            l.sort(reverse=True)
            print l
            bronze_award.threshold = l[(len(l) - 1) / 5]
            bronze_award.save()
            print "Created bronze", bronze_award
        general_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'priznanje',
            threshold = 0,
            defaults = {'template': 'priznanje',
                'serial_prefix': year_str + group_prefix
            },
        )

    def handle(self, *args, **options):
        try:
            first_arg = args[0]
        except:
            first_arg = None
        cslug = unicode(options.get('competition_slug', [first_arg])[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        attempt_awards = []
        for cqs in competition.competitionquestionset_set.all():
            max_score = cqs.questionset.questions.all().aggregate(
                Sum('max_score'))['max_score__sum']
            attempts_by_school = dict()
            all_attempts = list()
            confirmations = defaultdict(list)
            for c in AttemptConfirmation.objects.filter(
                    attempt__competitionquestionset=cqs).select_related('attempt'):
                confirmations[(c.by, c.attempt.access_code)].append(c)
            for stc in SchoolTeacherCode.objects.filter(
                    competition_questionset = cqs).select_related(
                        'teacher',
                        'school',
                        'code',
                    ):
                l = attempts_by_school.get(stc.school, [])
                for confirmation in confirmations[(stc.teacher, stc.code.value)]:
                    l.append(confirmation.attempt)
                    all_attempts.append(confirmation.attempt)
                attempts_by_school[stc.school] = l
            for j_year in JuniorYear.objects.filter(
                    questionset=cqs).select_related(
                        'mentorship__teacher',
                        'mentorship__school'
                    ):
                teacher = j_year.mentorship.teacher
                for confirmation in confirmations[(teacher, 'Beavers bridging brooks')]:
                    school = confirmation.attempt.juniorattempt.year_class.mentorship.school
                    l = attempts_by_school.get(school, [])
                    l.append(confirmation.attempt)
                    all_attempts.append(confirmation.attempt)
                    attempts_by_school[school] = l
            self.__create_awards(cqs, cqs.name, all_attempts, max_score)
            awards = Award.objects.filter(questionset = cqs)
            for school, attempts in attempts_by_school.iteritems():
                print "  ", school
                attempt_awards += assign_si_awards(attempts, awards, max_score)
        AttemptAward.objects.bulk_create(attempt_awards)
