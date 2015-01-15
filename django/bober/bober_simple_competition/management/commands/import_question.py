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
    def handle(self, *args, **options):
        dirname = args[0]
        q = Question.from_dir(dirname) 
        print q, q.resource_set.all()
