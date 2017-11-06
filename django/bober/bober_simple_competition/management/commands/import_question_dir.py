#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, sys
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify
from bober_simple_competition.models import *
from stat import S_ISDIR, ST_MODE
from optparse import make_option

class Command(BaseCommand):
    args = "<dirname>"
    help = "Add a whole questionset at a time"
    
    def add_arguments(self, parser):
        parser.add_argument('dirname', nargs='+', type=str)
    
    @transaction.atomic
    def handle(self, *args, **options):
        if len(args) > 0:
            dirname = unicode(options.get('dirname', [args[0]])[0])
        else:
            dirname = options['dirname'][0]
        mode = os.stat(dirname)[ST_MODE]
        if not S_ISDIR(mode):
            self.stderr.write("Not a directory")
            sys.exit(1)
        questions = []
        split_path = os.path.split(dirname)
        name = split_path[1]
        if name == '':
            name = os.path.split(split_path[0])[1]
        slug = slugify(name)
        for i in os.listdir(dirname):
            try:
                q = Question.from_dir(os.path.join(dirname, i))
                questions.append(q)
            except Exception as e:
                self.stdout.write("Error in {}: {}".format(i, e))
        self.stdout.write("created {}".format(slug))
        question_set, created = QuestionSet.objects.get_or_create(name = name, slug = slug)
        question_set.questions.clear()
        self.stdout.write("filling questionset")
        for q in questions:
            q_dict = Question.objects.filter(id = q.id).values_list()[0]
            self.stdout.write(str(q_dict))
            question_set.questions.add(q)
        question_set.rebuild_caches()
