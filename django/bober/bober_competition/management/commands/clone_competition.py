#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.management.base import BaseCommand
from django.db import transaction
import bober_competition.models


class Command(BaseCommand):
    # @transaction.atomic
    def handle(self, *args, **options):
        competition = bober_competition.models.Competition.objects.get(name = args[0])
        new_competition = bober_competition.models.Competition(name = args[1],
            active = 0, public_access = 0, 
            timestamp_start = competition.timestamp_start,
            timestamp_stop = competition.timestamp_stop,
            type = competition.type,
            duration = competition.duration)
        new_competition.save()
        # print new_competition.id
        # sid = transaction.savepoint()
        new_competition = bober_competition.models.Competition.objects.get(name=args[1])
        print new_competition.id
        for competition_question in competition.competitionquestion_set.all():
            new_competition_question = bober_competition.models.CompetitionQuestion(
                question = competition_question.question,
                competition = new_competition)
            new_competition_question.save()
            new_competition_question = bober_competition.models.CompetitionQuestion.objects.get(question = competition_question.question, competition=new_competition)
            print new_competition_question, new_competition_question.id
        #    sid2 = transaction.savepoint()
            for competition_question_category in competition_question.competitionquestioncategory_set.all():
                new_competition_question_category = bober_competition.models.CompetitionQuestionCategory(
                    competition_question = new_competition_question,
	            competition_category = competition_question_category.competition_category,
	            competiton_question_difficulty = competition_question_category.competiton_question_difficulty,)
                new_competition_question_category.save()
                print new_competition_question_category, new_competition_question_category.id
        #       sid3 = transaction.savepoint()
               
