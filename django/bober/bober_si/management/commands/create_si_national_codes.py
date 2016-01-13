#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from bober_si.models import *
from bober_simple_competition.models import AttemptConfirmation
from bober_paper_submissions.models import JuniorYear
import json
import os
from django.db.models import Sum



class Command(BaseCommand):
    # @transaction.atomic
    help = "Assign an award for each attempt in a list"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('school_competition_slug', nargs=1)
        parser.add_argument('national_competition_slug', nargs=1)

    def handle(self, *args, **options):
        if len(args) < 3:
            args += (None,) * (3 - len(args))
        scslug = unicode(options.get('school_competition_slug', [args[0]])[0])
        ncslug = unicode(options.get('national_competition_slug', [args[1]])[0])
        school_competition = SchoolCompetition.objects.get(slug=scslug)
        national_competition = SchoolCompetition.objects.get(slug=ncslug)
        organizer = national_competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        attempts_by_teacher = defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(list)))
        cqs_list = []
        for cqs in CompetitionQuestionSet.objects.filter(
                competition = national_competition).order_by('name'):
            school_cqs = CompetitionQuestionSet.objects.get(
                competition = school_competition,
                name = cqs.name)
            cqs_list.append(cqs)
            for a in Attempt.objects.filter(
                    competitionquestionset = school_cqs,
                    attemptaward__award__name = 'napreduje'):
                # print a.id, school_cqs
                if a.attemptaward_set.filter(award__name = 'napreduje', 
                        revoked_by=None).count() < 1:
                    # print "ha-ha!"
                    continue
                teacher = a.confirmed_by.all()[0]
                school = SchoolTeacherCode.objects.filter(
                    teacher = teacher,
                    competition_questionset = a.competitionquestionset,
                    code__value  = a.access_code
                )[0].school
                attempts_by_teacher[teacher][school][cqs].append(a)
        for teacher, school_dict in attempts_by_teacher.iteritems():
            for school, cqs_dict in school_dict.iteritems():
                # print school, cqs_dict
            # print teacher.user
                for cqs in cqs_list:
                    # print "    ", cqs
                    attempts = cqs_dict[cqs]
                    for a in attempts:
                        code = national_competition.competitor_code_create(
                            access_code = None,
                            competition_questionset = cqs,
                            code_data = {
                                'competitor_privileges':[
                                    'attempt',
                                    'resume_attempt',
                                ]
                            })
                        code.save()
                        short_code_value = code.value[
                            code.value.find(code.format.separator)+1:]
                        teacher.created_codes.add(code)
                        stc = SchoolTeacherCode(
                            competition_questionset = cqs,
                            school = school,
                            teacher = teacher,
                            code = code
                        )
                        stc.save()
                        school_name = school.name
                        teacher_name = u"{} {} <{}>".format(
                            teacher.user.first_name,
                            teacher.user.last_name,
                            teacher.user.email)
                        competitor_name = u"{} {}".format(
                            a.competitor.first_name,
                            a.competitor.last_name)
                        print u"\t".join([str(a.id), school.name, teacher_name, competitor_name, short_code_value]).encode('utf-8')
