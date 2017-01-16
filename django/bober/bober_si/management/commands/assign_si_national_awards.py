#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import F, ExpressionWrapper, fields
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
        parser.add_argument('competition_slug', nargs=1)
        parser.add_argument('questionset_name', nargs=1)

    def handle(self, *args, **options):
        if len(args) < 3:
            args += (None,) * (3 - len(args))
        cslug = unicode(options.get('competition_slug', [args[0]])[0])
        cqs_name = unicode(options.get('questionset_name', [args[1]])[0])
        cqss = CompetitionQuestionSet.objects.filter(
            competition__slug = cslug,
            name = cqs_name
        )
        competition = SchoolCompetition.objects.get(slug=cslug)
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        duration_expression = ExpressionWrapper(F('finish') - F('start'), output_field=fields.DurationField())
        for cqs in cqss:
            attempts = Attempt.objects.filter(
                competitionquestionset=cqs).exclude(
                    attemptconfirmation = None,
                ).annotate(duration=duration_expression).order_by("-score", "duration")
            # print attempts.query
            aawards = []
            for place, attempt in enumerate(attempts, start=1):
                print place, attempt.competitor, attempt.score, attempt.duration
                sct = SchoolTeacherCode.objects.filter(
                    competition_questionset=cqs,
                    code__value=attempt.access_code)[0]
                to_assign = set()
                for award in cqs.award_set.all():
                    if award.from_place is not None and place < award.from_place:
                        # print "place >=", award.from_place
                        continue
                    if award.min_threshold > attempt.score:
                        continue
                    if (award.to_place is not None and place <= award.to_place) \
                            or (award.threshold is not None and award.threshold <= attempt.score):
                        to_assign.add(award)
                print "  ", to_assign
                data = {'school_name': sct.school.display_name, 'revoked_by': organizer}
                assign_attempt_awards(attempt, to_assign, data, commit=True)
