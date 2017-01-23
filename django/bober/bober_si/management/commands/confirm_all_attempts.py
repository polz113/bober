#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation, Attempt
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Assign the award for the national championship, create .pdfs"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)
        parser.add_argument('questionset_name', nargs=1)

    def handle(self, *args, **options):
        if len(args) < 2:
            args += (None,) * (2 - len(args))
        cslug = unicode(options.get('competition_slug', [args[0]])[0])
        cqs_name = unicode(options.get('questionset_name', [args[1]])[0])
        competition = Competition.objects.get(slug=cslug)
        cqss = CompetitionQuestionSet.objects.filter(
            competition = competition,
            name = cqs_name
        )
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        # confirm attempts
        for cqs in cqss.all():   
            for attempt in Attempt.objects.filter(
                    competitionquestionset = cqs):
                mentor = organizer
                possible_mentors = SchoolTeacherCode.objects.filter(
                    code__value = attempt.access_code)
                if len(possible_mentors) == 1:
                    mentor = possible_mentors[0].teacher
                c, created = AttemptConfirmation.objects.get_or_create(
                    attempt = attempt,
                    defaults = {'by': mentor})
                if created:
                    c.save()
