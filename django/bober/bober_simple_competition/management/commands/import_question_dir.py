#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify
from bober_simple_competition.models import *
import os
from optparse import make_option

class Command(BaseCommand):
    args = "<dirname>"
    help = "Add a whole questionset at a time"
    def add_arguments(self, parser):
        parser.add_argument('dirname', nargs='+', type=str)
    @transaction.atomic
    def handle(self, *args, **options):
        dirname = unicode(options.get('dirname', [args[0]])[0])
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
            except Exception, e:
                print "Error in ", i, ":", e
        print "created", slug 
        question_set, created = QuestionSet.objects.get_or_create(name = name, slug = slug)
        question_set.questions.clear()
        print "filling questionset"
        for q in questions:
            q_dict = Question.objects.filter(id = q.id).values_list()[0]
            print q_dict
            question_set.questions.add(q)
        question_set.rebuild_caches()
