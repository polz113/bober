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
        parser.add_argument('competition_slug', nargs='1')
        parser.add_argument('questionset_name', nargs='1')

    def handle(self, *args, **options):
        if len(args) < 3:
            args += [None] * (3 - len(args))
        cslug = unicode(options.get('competition_slug', args[0])[0])
        cqs_name = unicode(options.get('questionset_name', args[1])[0])
        cqss = CompetitionQuestionSet.objects.filter(
            competition_slug = cslug,
            name = cqs_name
        )
        fname = unicode(options.get('attempt_list_filename', args[2])[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        for cqs in cqss:
            gold_award = Award.objects.get(
                name = 'zlato',
                questionset = cqs,)
            silver_award = Award.objects.get(
                name = 'srebrno',
                questionset = cqs)
            for attempt in Attempt.objects.filter(
                    competitionquestionset = cqs,
                ).exclude(
                    attemptconfirmation_set = None):
                attempt.grade_answers(update_graded = True,
                    regrade = True)
                first_name = attempt.competitor.first_name
                last_name = attempt.competitor.last_name
                duration = attempt.finish - attempt.start
                score = attempt.score
                sct = SchoolTeacherCode.objects.filter(
                    competition_questionset = cqs,
                    code__value = attempt.access_code)[0]
                max_score = cqs.questionset.questions.all().aggregate(
                    Sum('max_score'))['max_score__sum']

                school = sct.school
                teacher = sct.teacher
                # Veselo kodiranje, Janez!
                # Spodaj je primer, kako se dodeli zlato priznanje.
                award = gold_award
                serial = "{}{:06}".format(award.serial_prefix, attempt.id)
                aa = AttemptAward(
                    award = award,
                    attempt = attempt,
                    competitor_name = u" ".join([first_name, last_name]),
                    school_name = school.name,
                    group_name = award.group_name,
                    serial = serial)
