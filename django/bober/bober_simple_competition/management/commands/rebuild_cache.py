#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.db import transaction
from bober_simple_competition.models import *
import json
import os

class Command(BaseCommand):
    # @transaction.atomic

    def make_manifest(dirname):
        pass
    
    def add_arguments(self, parser):
        parser.add_argument('questionset_slug', type=str)
        
    def handle(self, *args, **options):
        qs = QuestionSet.objects.get(slug = options['questionset_slug'])
        qs.rebuild_caches()
