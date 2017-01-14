#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.db import transaction
from bober_simple_competition.models import *
import json
import os

class Command(BaseCommand):
    # @transaction.atomic
    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)
        parser.add_argument('questionset_name', nargs=1)
    
    def make_manifest(dirname):
        pass

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
        cslug = args[0]
        competition = Competition.objects.get(slug=cslug)
        competition.grade_answers(regrade=True, update_graded=True)
        for cqs in cqss:
            for attempt in Attempt.objects.filter(
                        competitionquestionset = cqs
                    ).exclude(confirmed_by = None):
                attempt.score = attempt.latest_answers_sum()
                attempt.save()
