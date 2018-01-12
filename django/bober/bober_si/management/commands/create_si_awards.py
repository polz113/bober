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
    help = "Create awards for a slovenian school-level competition"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs='+')

    def __create_awards(self, cqs):
        self.stdout.write("creating for {}".format(cqs))
        max_score = cqs.questionset.questions.all().aggregate(
            Sum('max_score'))['max_score__sum']
        group_name = cqs.name
        year_str = str(timezone.now().year)[-2:]
        group_prefix = {
            '1. letnik': '11',
            '2. letnik': '12',
            '3. letnik': '13',
            '4. letnik': '14',
            '1. razred': '01',
            '2. razred': '02',
            '3. razred': '03',
            '4. razred': '04',
            '5. razred': '05',
            '6. razred': '06',
            '7. razred': '07',
            '8. razred': '08',
            '9. razred': '09',
        }.get(group_name, slugify(group_name))
        if max_score is None:
            max_score = 10
        bronze_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'bronasto',
            defaults = {
                'template': 'bronasto',
                'threshold': max_score,
                'min_threshold': max_score // 2,
                'serial_prefix': year_str + group_prefix + 'B',
            }
        )
        if created or True:
            # set the threshold to cover 1/5 of all competitors
            l = Attempt.objects.filter(
                    competitionquestionset = cqs
                ).exclude(
                    confirmed_by = None
                ).order_by('-score').values_list('score', flat=True)
            self.stdout.write("{}: {}".format(bronze_award, l))
            bronze_award.threshold = l[(len(l) - 1) // 5]
            bronze_award.save()
            self.stdout.write("Created bronze {}".format(bronze_award))
        general_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'priznanje',
            defaults = {
                'threshold': 0,
                'template': 'priznanje',
                'min_threshold': 0.0,        
                'serial_prefix': year_str + group_prefix + 'P'
            },
        )
        bronze_award.replaces.add(general_award)
        promoted_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'napreduje',
            defaults = {
                'threshold': max_score,
                'min_threshold': max_score,
                'serial_prefix': year_str + group_prefix + 'N',
            }
        )
        
        
    def handle(self, *args, **options):
        try:
            first_arg = args[0]
        except:
            first_arg = None
        cslug = options.get('competition_slug', [first_arg])[0]
        competition = SchoolCompetition.objects.get(slug=cslug)
        for cqs in competition.competitionquestionset_set.all():
            self.__create_awards(cqs)
