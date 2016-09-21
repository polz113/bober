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
        parser.add_argument('competition_slug', type=str)
        parser.add_argument('username', nargs='?', type=str)
        
    def handle(self, *args, **options):
        c = Competition.objects.get(slug = options['competition_slug'])
        code = c.master_code_create()
        if 'username' in options:
            p = Profile.objects.get(user__username = options['username'])
            p.created_codes.add(code)
            p.received_codes.add(code)
        print(code.value)
