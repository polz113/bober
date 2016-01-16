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


    def __create_awards(self, cqs):
        print "creating for", cqs
        max_score = cqs.questionset.questions.all().aggregate(
            Sum('max_score'))['max_score__sum']
        group_name = cqs.name
        year_str = str(timezone.now().year)[-2:]
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
        }.get(group_name, slugify(group_name))
        first_place_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'prva',
            defaults = {
                'threshold': 0.0,
                'template': 'prva',
                'serial_prefix': year_str + group_prefix + '1',
            }
        )
        second_place_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'druga',
            defaults = {
                'threshold': 0.0,
                'template': 'druga',
                'serial_prefix': year_str + group_prefix + '2',
            }
        )
        third_place_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'tretja',
            defaults = {
                'threshold': 0.0,
                'template': 'tretja',
                'serial_prefix': year_str + group_prefix + '3',
            }
        )
        gold_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'zlato',
            defaults = {
                'threshold': 0.0,
                'template': 'zlato',
                'serial_prefix': year_str + group_prefix + 'G',
            }
        )
        silver_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'srebrno',
            defaults = {
                'threshold': 0.0,
                'template': 'srebrno',
                'serial_prefix': year_str + group_prefix + 'P',
            },
        )

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
            self.__create_awards(cqs)
            # Janez, ustvariti je treba nagrade.
            gold_award = Award.objects.get(
                name = 'zlato',
                questionset = cqs)
            silver_award = Award.objects.get(
                name = 'srebrno',
                questionset = cqs)
            awards = (silver_award, gold_award)
            attempts = Attempt.objects.filter(
                competitionquestionset=cqs).exclude(
                    attemptconfirmation = None,
                )
            first_awards = []
            for name in 'prva', 'druga', 'tretja':
                first_awards.append(Award.objects.get(
                    name=name, 
                    questionset=cqs))
            data = []
            for attempt in attempts:
                attempt.grade_answers(update_graded=True, regrade=True)
                first_name = attempt.competitor.first_name
                last_name = attempt.competitor.last_name
                duration = attempt.finish - attempt.start
                n_correct = attempt.gradedanswer_set.filter(score=1.0).count()
                attempt.score = n_correct
                attempt.save()
                print attempt.access_code
                sct = SchoolTeacherCode.objects.filter(
                    competition_questionset=cqs, 
                    code__value=attempt.access_code)
                if len(sct) == 1:
                    sct = sct[0]
                    data.append((attempt.score, -duration, attempt.id,
                              first_name + u" " + last_name, sct.school, sct.teacher))
                else:
                    print "PROBLEM:", attempt.id, attempt.access_code
                    data.append((attempt.score, -duration, attempt.id,
                              first_name + u" " + last_name, '', ''))
            data.sort(reverse=True)
            n_attempts = len(data)
            # with 4 competitors, (3 - 1) // 4 = 0, so the 0th (+ tied) gets gold
            # with 5, (8 - 1) // 4 = 1 so the 0th and 1st (+tied) get gold
            # with 8, (8 - 1) // 4 = 1, so the 0th and 1st (+ tied) get gold
            # with 9, (9 - 1) // 4 = 2, so 0th, 1st and 2nd (+ tied) get gold
            gold_thresh = data[(n_attempts - 1) // 4][0]
            if gold_thresh != gold_award.threshold:
                gold_award.threshold = gold_thresh
                gold_award.save()
            silver_thresh = data[(n_attempts - 1) // 2][0]
            if silver_thresh != silver_award.threshold:
                silver_award.threshold = silver_thresh
                silver_award.save()
            print data
            for i, (score, duration, aid, name, school, teacher) in enumerate(data):
                if i < len(first_awards):
                    award = first_awards[i]
                    serial = "{}{:06}".format(award.serial_prefix, aid)
                    aa = AttemptAward(
                        award=award, attempt_id=aid, competitor_name=name,
                        school_name=school, group_name=award.group_name, serial=serial)
                    aa.save()
                    print "    ", aa
                if score < silver_thresh:
                    break 
                is_gold = score >= gold_thresh
                award = awards[is_gold]
                serial = "{}{:06}".format(award.serial_prefix, attempt.id)
                aa = AttemptAward(
                    award=award, attempt_id=aid, competitor_name=name,
                    school_name=school, group_name=award.group_name, serial=serial)
                aa.save()
                print "    ", aa
            # Manjka se izpis priznanj za prve tri. Kako bomo naredili to?
