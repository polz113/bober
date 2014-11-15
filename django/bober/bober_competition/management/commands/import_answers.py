#!/usr/bin/python
# -*- coding: utf8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.management.base import BaseCommand
from django.db import transaction
import bober_competition.models
import os
import time, datetime
from django.utils.timezone import utc


class Command(BaseCommand):
    # @transaction.atomic
    def handle(self, *args, **options):
        competition = bober_competition.models.Competition.objects.get(name = args[0])
        dirname = args[1]
        answers = list()
        # read all lines into answers
        for i in os.listdir(dirname):     
            with open(os.path.join(dirname, i)) as f:
                for l in f.readlines():
                    try:
                        (competition_user_id, question_id, custom_answer, timestamp_str) = l.split(';')
                        dt = datetime.datetime.strptime(timestamp_str.strip(), '%Y-%m-%d %H:%M:%S')
                        dt = dt.replace(tzinfo = utc)
                        t = (dt, competition_user_id, question_id, custom_answer)
                        answers.append(t)
                    except ValueError, e:
                        print i, e, l
        # sort by timestamp, competition_user_id, question_id, answer
        answers.sort()
        # remove duplicates
        last_answers = dict()
        for i in answers:
            key = (i[1],i[2])
            if key in last_answers:
                if last_answers[key][1] == i[0] and last_answers[key][0] != i[3]:
                    print "Two answers in one second, ", key, last_answers[key][0], i[3]
            last_answers[key] = (i[3], i[0])
        print len(last_answers)
        print answers[-1]
        for (competition_user_id, question_id), (custom_answer, timestamp) in last_answers.iteritems():
            c = bober_competition.models.CompetitionUserQuestion.objects.get(competition_user_id = competition_user_id,
                competition_question__question__id = question_id)
            print c, "->", (custom_answer, timestamp)
            if c.last_change is None or c.last_change < timestamp:
                c.last_change = timestamp
                c.custom_answer = custom_answer
                c.save()
