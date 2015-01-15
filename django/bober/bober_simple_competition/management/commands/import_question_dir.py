#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify
from bober_simple_competition.models import *
import os

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        dirname = unicode(args[0])
        questions = []
        name = os.path.split(dirname)[-1]
        slug = slugify(name)
        for i in os.listdir(dirname):
            try:
                q = Question.from_dir(os.path.join(dirname, i))
                questions.append(q)
            except Exception, e:
                print "Error:", e
                pass
        
        question_set, created = QuestionSet.objects.get_or_create(name = name, slug = slug)
        for q in questions:
            q_dict = Question.objects.filter(id = q.id).values_list()[0]
            print q_dict
            question_set.questions.add(q)
        question_set.rebuild_caches()
