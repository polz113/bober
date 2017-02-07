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
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        attempt_awards = []
        revoked_awards = []
        for school in School.objects.filter(
                    schoolteachercode__competition_questionset__competition = competition
                ).distinct():
            awards = Award.objects.filter(questionset__competition = competition)
            new_awards, revoke_awards = school.assign_si_awards(awards, 
                competition.competitionquestionset_set.all(), 
                revoked_by = organizer, commit = False)
            attempt_awards += new_awards
            revoked_awards += revoke_awards
        revoked_ids = list()
        for award in revoked_awards:
            revoked_ids.append(award.id)
        print "    revoking:", revoked_ids
        AttemptAward.objects.filter(id__in = revoked_ids).update(
            revoked_by = organizer)
        print "    new:", attempt_awards
        AttemptAward.objects.bulk_create(attempt_awards)
