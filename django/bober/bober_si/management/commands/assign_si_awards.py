#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation
import json
import os
from django.db.models import Sum

def __create_awards(competition, group_name, all_attempts):
    bronze_award, created = Award.objects.get_or_create(
        # questionset = cqs,
        competition = competition,
        group_name = group_name,
        template = 'bronasto',
        name = 'bronasto',
        defaults = {
            'threshold':max_score,
            'serial_prefix':year_prefix + cqs.name[:2]
        }
    )
    if created:
        l = []
        for a in all_attempts:
            l.append(a.score)
        l.sort(reverse=True)
        bronze_award.threshold = l[(len(l) - 1) / 5] 
        bronze_award.save()
    general_award, created = Award.objects.get_or_create(
        # questionset = cqs,
        competition = competition,
        group_name = group_name,
        name = 'priznanje',
        threshold = 0,
        defaults = {'template': 'priznanje'},
    )


class Command(BaseCommand):
    # @transaction.atomic
    help = "Assign awards according to slovenian rules"
    def make_manifest(dirname):
        print "haha"
    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs='+')

    def handle(self, *args, **options):
        try:
            first_arg = args[0]
        except:
            first_arg = None
        cslug = unicode(options.get('competition_slug', [first_arg])[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        attempt_awards = []
        year_str = str(timezone.now().year)[-2:]
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
                    l.append(confirmation)
                    if bronze_award is None:
                        all_attempts.append(confirmation.attempt)
                attempts_by_school[stc.school] = l
            __create_awards(cqs.competition, cqs.name, all_attempts)
            awards = Award.objects.filter(questionset = cqs)
            for school, attempts in attempts_by_school.iteritems():
                print "  ", school
                attempt_awards += assign_si_awards(attempts, awards)
        AttemptAward.objects.bulk_create(attempt_awards)
