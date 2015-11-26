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
        cslug = unicode(options.get('competition_slug', first_arg)[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        attempt_awards = []
        year_str = str(timezone.now().year)[-2:]
        for cqs in competition.competitionquestionset_set.all():
            max_score = cqs.questionset.questions.all().aggregate(
                Sum('max_score'))['max_score__sum']
            attempts_by_school = dict()
            all_attempts = list()
            try:
                bronze_award = cqs.award_set.get(
                    name='bronasto')
            except Exception, e:
                print "E:", e
                bronze_award = None
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
                        all_attempts.append(confirmation)
                attempts_by_school[stc.school] = l
            if bronze_award is None:
                l = []
                for c in all_attempts:
                    l.append(c.attempt.score)
                l.sort(reverse=True)
                bronze_award = Award(
                    questionset = cqs,
                    template = 'bronasto',
                    name = 'bronasto',
                    threshold = l[(len(l) - 1) / 5]
                    serial_prefix = year_prefix + cqs.name[:2]
                )
                bronze_award.save()
            general_award, created = Award.objects.get_or_create(
                questionset = cqs,
                name = 'priznanje',
                threshold = 0,
                defaults = {'template': 'priznanje'},
            )
            print bronze_award.threshold
            for school, confirmations in attempts_by_school.iteritems():
                print "  ", school
                l = []
                for c in confirmations:
                    l.append((c.attempt.score, c))
                    # print "    ", c.attempt.competitor, c.attempt.access_code, c.by
                l.sort(reverse=True)
                if len(l) < 1:
                    continue
                bronze_threshold = min(l[(len(l) - 1) // 3], bronze_award.threshold)
                bronze_threshold = max(bronze_threshold, max_score / 2)
                for i in l:
                    a = i[1].attempt
                    if i[0] >= bronze_threshold:
                        attempt_awards.append(
                            AttemptAward(
                                award = bronze_award,
                                attempt = a,
                                serial = bronze_award.serial_prefix + str(a.id)
                            )
                        )
                    else:
                        attempt_awards.append(
                            AttemptAward(
                                award = general_award,
                                attempt = a,
                                serial = bronze_award.serial_prefix + str(a.id)
                            )
                        )
        AttemptAward.objects.bulk_create(attempt_awards)
