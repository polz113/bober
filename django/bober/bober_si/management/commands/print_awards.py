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
            for award in cqs.award_set.order_by('-threshold'):
                print "{}\n\r".format(award.name.encode("utf-8")),
                for aaward in award.attemptaward_set.filter(
                        revoked_by = None).order_by(
                        'attempt__competitor__last_name',
                        'attempt__competitor__first_name',
                    ):
                    print u"{} {}\n\r".format(
                        aaward.attempt.competitor.first_name,
                        aaward.attempt.competitor.last_name).title().encode('utf-8'),

