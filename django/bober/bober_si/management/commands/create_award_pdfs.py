#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.models import *
from bober_si.award_gen import generate_award_pdf
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Create all award .pdfs in a single file"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)
        parser.add_argument('questionset_name', nargs=1)
        parser.add_argument('output_filename', nargs=1)

    def handle(self, *args, **options):
        if len(args) < 3:
            args += (None,) * (3 - len(args))
        cslug = unicode(options.get('competition_slug', [args[0]])[0])
        cqs_name = unicode(options.get('questionset_name', [args[1]])[0])
        output_filename = unicode(options.get('output_filename', [args[2]])[0])
        cqss = CompetitionQuestionSet.objects.filter(
            competition__slug = cslug,
            name = cqs_name
        )
        competition = SchoolCompetition.objects.get(slug=cslug)
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        data = []
        for cqs in cqss:
            attempts = Attempt.objects.filter(
                competitionquestionset=cqs).exclude(
                    attemptconfirmation = None,
                )
            awards = AttemptAward.objects.filter(
                attempt__competitionquestionset = cqs, 
            ).order_by(
                'attempt__competitor__last_name',
                'attempt__competitor__first_name'
            ).select_related(
                'award')
            for award in awards:
                data.append(
                {
                    'name': award.competitor_name,
                    'school': award.school_name,
                    'group': award.group_name,
                    'serial': award.serial,
                    'template': award.award.template,
                })
        template_file = os.path.join(AWARD_TEMPLATE_DIR, 'all_si.svg')
        generate_award_pdf(output_filename,
            data, template_file)

