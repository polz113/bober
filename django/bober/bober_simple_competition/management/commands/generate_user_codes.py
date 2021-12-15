#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User

class Command(BaseCommand):
    # @transaction.atomic

    def make_manifest(dirname):
        pass
    
    def add_arguments(self, parser):
        parser.add_argument('competition_slug', type=str)
        parser.add_argument('questionset_name', type=str)
        parser.add_argument('master_code', type=str)
        parser.add_argument('n_of_codes', type=int)
        
    def handle(self, n_of_users, **options):
        cslug = options.get('competition_slug')
        cqs_name = options.get('questionset_name')
        master_code = options.get('master_code')
        n_of_codes = options.get('n_of_codes')
        competition = Competition.objects.get(slug=cslug)
        cqss = CompetitionQuestionSet.objects.filter(
            competition = competition,
            name = cqs_name
        )
        for cqs in cqss:
            code_data = competition.max_competitor_code_data(master_code)
            code_data['competition_questionset'] = [
                cqs.slug_str()
            ]
            for i in range(n_of_codes):
                c = competition.competitor_code_generator.create_code(code_data)
                c.save()
