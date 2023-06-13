#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.models import *
from bober_si.award_util import create_si_national_awards
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Create the awards for slovenian national championships"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)
    def handle(self, *args, **options):
        if len(args) < 1:
            args += (None,) * (3 - len(args))
        cslug = options.get('competition_slug', [args[0]])[0]
        competition = SchoolCompetition.objects.get(slug=cslug)
        for cqs in competition.competitionquestionset_set.all():
            create_si_national_awards(cqs)
