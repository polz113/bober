#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation
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
        cslug = unicode(options.get('competition_slug', first_arg)[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        
