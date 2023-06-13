#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.award_util import create_si_awards
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Create awards for a slovenian school-level competition"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs='+')
        
    def handle(self, *args, **options):
        try:
            first_arg = args[0]
        except:
            first_arg = None
        cslug = options.get('competition_slug', [first_arg])[0]
        competition = SchoolCompetition.objects.get(slug=cslug)
        for cqs in competition.competitionquestionset_set.all():
            create_si_awards(cqs)

