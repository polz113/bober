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
    help = "Create the awards for slovenian national championships"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)


    def __create_awards(self, cqs):
        print ("creating for", cqs)
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
        l = list(Attempt.objects.filter(
            competitionquestionset = cqs
        ).exclude(
            confirmed_by = None
        ).order_by('-score').values_list('score', flat=True))
        first_place_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'prva',
            defaults = {
                'threshold': None,
                'min_threshold': 0.0,
                'from_place': 1,
                'to_place': 1,
                'template': 'prva',
                'serial_prefix': year_str + group_prefix + '1',
            }
        )
        second_place_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'druga',
            defaults = {
                'threshold': None,
                'min_threshold': 0.0,
                'from_place': 2,
                'to_place': 2,
                'template': 'druga',
                'serial_prefix': year_str + group_prefix + '2',
            }
        )
        third_place_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'tretja',
            defaults = {
                'threshold': None,
                'min_threshold': 0.0,
                'from_place': 3,
                'to_place': 3,
                'template': 'tretja',
                'serial_prefix': year_str + group_prefix + '3',
            }
        )
        gold_award, gold_created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'zlato',
            defaults = {
                'threshold': None,
                'min_threshold': 0.0,
                'template': 'zlato',
                'serial_prefix': year_str + group_prefix + 'G',
            }
        )
        print (cqs, l)
        if len(l) < 1:
            return
        silver_defaults = {
            'threshold': l[(len(l)-1)//2],
            'min_threshold': 0.0,
            'template': 'srebrno',
            'serial_prefix': year_str + group_prefix + 'S',
        }
        if gold_award.to_place is not None:
            silver_defaults['from_place'] = gold_award.to_place+1
        silver_award, created = Award.objects.get_or_create(
            questionset = cqs,
            group_name = group_name,
            name = 'srebrno',
            defaults = silver_defaults
        )
        gold_award.replaces.add(silver_award)
        try:
            bronze_award = Award.objects.get(
                questionset = cqs,
                name = 'bronasto')
            silver_award.replaces.add(bronze_award)
            gold_award.replaces.add(bronze_award)
        except:
            pass
        try:
            general_award = Award.objects.get(
                questionset = cqs,
                name = 'priznanje')
            silver_award.replaces.add(general_award)
            gold_award.replaces.add(general_award)
        except:
            pass
        
    def handle(self, *args, **options):
        if len(args) < 1:
            args += (None,) * (3 - len(args))
        cslug = options.get('competition_slug', [args[0]])[0]
        competition = SchoolCompetition.objects.get(slug=cslug)
        for cqs in competition.competitionquestionset_set.all():
            self.__create_awards(cqs)
