#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Assign an award for each attempt in a list"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)
        parser.add_argument('questionset_name', nargs=1)

    def handle(self, *args, **options):
        if len(args) < 3:
            args += (None,) * (3 - len(args))
        cslug = unicode(options.get('competition_slug', [args[0]])[0])
        cqs_name = unicode(options.get('questionset_name', [args[1]])[0])
        cqss = CompetitionQuestionSet.objects.filter(
            competition__slug = cslug,
            name = cqs_name
        )
        competition = SchoolCompetition.objects.get(slug=cslug)
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        for cqs in cqss:
            # Janez, ustvariti je treba nagrade.
            gold_award = Award.objects.get(
                name = 'zlato',
                questionset = cqs)
            silver_award = Award.objects.get(
                name = 'srebrno',
                questionset = cqs)
            awards = (silver_award, gold_award)
            attempts = Attempt.objects.filter(competitionquestionset=cqs)
            data = []
            for attempt in attempts:
                attempt.grade_answers(update_graded=True, regrade=True)
                first_name = attempt.competitor.first_name
                last_name = attempt.competitor.last_name
                duration = attempt.finish - attempt.start
                sct = SchoolTeacherCode.objects.filter(
                    competition_questionset=cqs, code__value=attempt.access_code)[0]
                data.append(attempt.score, -duration, attempt.id
                              first_name + u" " + last_name, sct.school, sct.teacher)
            data.sort(reverse=True)
            n_attemps = len(data)
            # with 4 competitors, (3 - 1) // 4 = 0, so the 0th (+ tied) gets gold
            # with 5, (8 - 1) // 4 = 1 so the 0th and 1st (+tied) get gold
            # with 8, (8 - 1) // 4 = 1, so the 0th and 1st (+ tied) get gold
            # with 9, (9 - 1) // 4 = 2, so 0th, 1st and 2nd (+ tied) get gold
            gold_thresh = data[(n_attempts - 1) // 4][0]
            silver_thresh = data[(n_attempts - 1) // 2][0]
            awarded_names = ([], []) # names of those getting (silver, gold)
            for score, duration, aid, name, school, teacher in data:
                if score < silver_thresh:
                    break
                is_gold = score >= gold_thresh
                award = awards[is_gold]
                awarded_names[is_gold].append(name)
                serial = "{}{:06}".format(award.serial_prefix, aid)
                aa = AttemptAward(
                    award=award, attempt=attempt, competitor_name=name,
                    school_name=school, group_name=award.group_name, serial=serial)
            print("Gold awards", "\n".join(sorted(awarded_names[1]))
            print("Silver awards", "\n".join(sorted(awarded_names[0]))
            i = 3
            while i < n_attempts and scores[i][:2] == scores[i - 1][:2]: # while tied
                i += 1
            print("First three", "\n".join("%s, %s (%i, %i)" % (a[3], a[4], a[0], -a[1])
                                           for a in scores)
            # Manjka se izpis priznanj za prve tri. Kako bomo naredili to?
