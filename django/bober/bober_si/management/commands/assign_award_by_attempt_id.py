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
        parser.add_argument('award_name', nargs=1)
        parser.add_argument('attempt_list_filename', nargs=1)

    def handle(self, *args, **options):
        if len(args) < 3:
            args += (None,) * (3 - len(args))
        cslug = unicode(options.get('competition_slug', [args[0]])[0])
        award_name = unicode(options.get('award_name', [args[1]])[0])
        fname = unicode(options.get('attempt_list_filename', [args[2]])[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        with open(fname) as f:
            attempt_ids = f.read().split()
        awards = Award.objects.filter(questionset__competition = competition,
                name = award_name)
        # print attempt_ids
        for award in awards:
            for attempt in Attempt.objects.filter(
                    competitionquestionset = award.questionset,
                    id__in = attempt_ids).exclude(
                    confirmed_by = None):
                c = attempt.competitor
                serial = "{}{:06}".format(award.serial_prefix, attempt.id)
                aa = AttemptAward(award = award,
                    attempt = attempt,
                    competitor_name = u" ".join([c.first_name, c.last_name]),
                    group_name = award.questionset.name,
                    serial = serial)
                aa.save()
            #for school, attempts in attempts_by_school.items():
            #    print "  ", school
            #    new_awards, revoke_awards = assign_si_awards(attempts, awards, max_score)
            #    attempt_awards += new_awards
            #    revoked_awards += revoke_awards
