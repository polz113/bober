#!/usr/bin/python
# -*- coding: utf8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.management.base import BaseCommand

import bober_competition


class Command(BaseCommand):
    def handle(self, *args, **options):
        competition = bober_competition.models.Competition.objects.get(name = args[0])
        new_competition = bober_compettition.models.Competition(name = args[1],
            active = 0, 
            timestamp_start = competition.timestamp_start,
            timestamp_stop = competition.timestamp_stop,
            type = competition.type,
            duration = competition.duration)
        new_competition.save()
        for competition_question in competition.competitionquestion_set.all():
            competition_question.id = None
            competition_question.competition = new_competition
        for competition_category in competition.competitioncategoryactive_set.all():
            competition_question_categories = list(competition_category.competitionquestioncategory_set.all())
            new_competition_category = competition_category
            new_competition_category.id = None
            new_competition_category.competition = new_competition
            new_competition_category.save()
            for q in competition_question_categories:
                q.id = None
                q.competition_category = new_competition_category
                q.save()
            
