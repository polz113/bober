#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.models import *
from bober_si.award_util import create_teacher_awards
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
import re
from django.db.models import Sum

class Command(BaseCommand):
    # @transaction.atomic
    help = "Create the teacher certificates for a slovenian competition"

    def make_manifest(dirname):
        pass
        # print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)

    def __create_awards(self, cqs):
        pass

    def handle(self, *args, **options):
        if len(args) < 1:
            args += (None,) * (3 - len(args))
        cslug = options.get('competition_slug', [args[0]])[0]
        competition = SchoolCompetition.objects.get(slug=cslug)
        create_teacher_awards(competition)

