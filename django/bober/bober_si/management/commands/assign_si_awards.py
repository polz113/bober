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
    help = "Assign awards according to slovenian rules"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs='+')

    def __create_awards(self, cqs):
        print "creating for", cqs
        max_score = cqs.questionset.questions.all().aggregate(
            Sum('max_score'))['max_score__sum']
        group_name = cqs.name
        year_str = str(timezone.now().year)[-2:]
        group_prefix = {
            '1. letnik': '11',
            '2. letnik': '12',
            '3. letnik': '13',
            '4. letnik': '14',
            '1. razred': '01',
            '2. razred': '02',
            '3. razred': '03',
            '4. razred': '04',
            '5. razred': '05',
            '6. razred': '06',
            '7. razred': '07',
            '8. razred': '08',
            '9. razred': '09',
        }.get(group_name, slugify(group_name))
        bronze_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            template = 'bronasto',
            name = 'bronasto',
            defaults = {
                'threshold': max_score,
                'serial_prefix': year_str + group_prefix + 'B',
            }
        )
        if created:
            l = Attempt.objects.filter(
                    competitionquestionset = cqs
                ).order_by('-score').values_list(score, flat=True)
            print l
            bronze_award.threshold = l[(len(l) - 1) / 5]
            bronze_award.save()
            print "Created bronze", bronze_award
        general_award, created = Award.objects.get_or_create(
            questionset = cqs,
            competition = cqs.competition,
            group_name = group_name,
            name = 'priznanje',
            threshold = 0,
            defaults = {'template': 'priznanje',
                'serial_prefix': year_str + group_prefix + 'P'
            },
        )

    def handle(self, *args, **options):
        try:
            first_arg = args[0]
        except:
            first_arg = None
        cslug = unicode(options.get('competition_slug', [first_arg])[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
        attempt_awards = []
        revoked_awards = []
        for cqs in competition.competitionquestionset_set.all():
            self.__create_awards(cqs)
        for school in School.objects.filter(
                    schoolteachercode__competitionquestionset__competition = competition
                ).distinct():
            awards = Award.objects.filter(questionset__competition = competition)
            new_awards, revoke_awards = school.assign_si_awards(awards, 
                competition.competitionquestionset_set.all(), 
                revoked_by = organizer, commit = False)
            attempt_awards += new_awards
            revoked_awards += revoke_awards
            #for school, attempts in attempts_by_school.iteritems():
            #    print "  ", school
            #    new_awards, revoke_awards = assign_si_awards(attempts, awards, max_score)
            #    attempt_awards += new_awards
            #    revoked_awards += revoke_awards
        revoked_ids = list()
        for award in revoked_awards:
            revoked_ids.append(award.id)
        print "    revoking:", revoked_ids
        AttemptAward.objects.filter(id__in = revoked_ids).update(
            revoked_by = organizer)
        print "    new:", attempt_awards
        AttemptAward.objects.bulk_create(attempt_awards)
