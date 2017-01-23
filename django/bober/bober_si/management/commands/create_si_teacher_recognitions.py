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

DEFAULT_TEXT_TEMPLATE = u"""{name} je bil(a) mentor(ica)
{n_confirmed}.
{award_listing}
"""

TEXT_TEMPLATES = {
    "solsko-2016": u"""{name} 
je bil(a) na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo med 7. novembrom in 11. novembrom 2016, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
    "drzavno-2016":u"""{name} je bil(a) mentor(ica) na državnem nivoju 
{n_confirmed}.
{award_listing}
{top_places_listing}
""",
}


def _compose_text(teacher, attempts, template):
    # a poor man's slovenian gettext pluralization by Janez Demsar
    class Plural:
        def __init__(self, *forms):
            self.forms = forms

        def __getitem__(self, n):
            n %= 100
            if n == 4: n = 3
            elif n >= 5: n = 4
            n -= 1
            if n >= len(self.forms): n = 2
            return self.forms[n]

    class Numbers:
        def __init__(self, *forms):
            self.forms = forms

        def __getitem__(self, n):
            return self.forms[n - 1] if n - 1 < len(self.forms) else str(n)
    p_tekmovalcu = Plural(u"tekmovalcu", u"tekmovalcema", u"tekmovalcem")
    p_tekmovalec = Plural(u"tekmovalec", u"tekmovalca", u"tekmovalci", u"tekmovalcev")
    p_je = Plural(u"je", u"sta", u"so", u"je")
    p_se_je = Plural(u"se je", u"sta se", u"so se", u"se je")
    p_osvojil = Plural(u"osvojil", u"osvojila", u"osvojili", u"osvojilo")
    p_uvrstil = Plural(u"uvrstil", u"uvrstila", u"uvrstili", u"uvrstilo")
    n_nom = Numbers(u"En", u"Dva", u"Trije", u"Štirje", u"Pet", u"Šest", u"Sedem", u"Osem", u"Devet")
    n_dativ = Numbers(u"enemu", u"dvema", u"trem", u"štirim", u"petim", u"šestim", u"sedmim", u"osmim", u"devetim")
    # end of slovenian language gettext replacement
    # texts are pretty much hard-coded here
    n_school = attempts.count()
    if n_school <= 0:
        return ''
    n_confirmed = n_dativ[n_school] + u" " + p_tekmovalcu[n_school]
    next_round_listing = u""
    awards = AttemptAward.objects.filter(
        revoked_by = None,
        attempt__id__in=attempts.values_list('id', flat=True)
    ).distinct()
    n = awards.filter(award__name="napreduje").distinct().count()
    if n > 0:
        next_round_listing = u"{} {} {} {} na državno tekmovanje.\n".format(
                n_nom[n], p_tekmovalec[n], p_se_je[n], p_uvrstil[n])
    award_listing = []
    for award_name in ["bronasto", "srebrno", "zlato"]:
        n = awards.filter(award__name=award_name).distinct().count()
        if n > 0:
            award_listing.append(
                u"{} {} {} {} priznanje.\n".format(
                    n_nom[n], p_je[n], p_osvojil[n], award_name))
    award_listing = u"\n".join(award_listing)
    top_places_listing = []
    for award_name, nm in [
                ("prva", "prvo"), 
                ("druga", "drugo"),
                ("tretja", "tretje")]:
        n = awards.filter(award__name=award_name).distinct().count()
        if n > 0:
            if len(top_places_listing) == 0:
                top_places_listing.append("Uvrstitve:")
            top_places_listing.append("- {} {} {} {} na {} mesto".format(
                   n_nom[n], p_tekmovalec[n], p_se_je[n], p_uvrstil[n], nm)
            )
    top_places_listing = u"\n".join(top_places_listing)
    name = u"{} {}".format(teacher.user.first_name, teacher.user.last_name)
    return template.format(**locals())

class Command(BaseCommand):
    # @transaction.atomic
    help = "Create the teacher certificates for a slovenian competition"

    def make_manifest(dirname):
        print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)


    def __create_awards(self, cqs):
        pass

    def handle(self, *args, **options):
        if len(args) < 1:
            args += (None,) * (3 - len(args))
        cslug = unicode(options.get('competition_slug', [args[0]])[0])
        competition = SchoolCompetition.objects.get(slug=cslug)
        template = TEXT_TEMPLATES.get(cslug, DEFAULT_TEXT_TEMPLATE)
        for teacher in Profile.objects.filter(schoolteachercode__competition_questionset__competition = competition).distinct():
            print("----------------------------")
            print(teacher, teacher.user.email)
            print("----------------------------")
            attempts = Attempt.objects.filter(
                    competitionquestionset__competition = competition, 
                    confirmed_by=teacher
                ).distinct()
            if False:
                # consider only attempts confirmed only by the mentor
                attempts = attempts.annotate(
                    n_confirmations = Count('confirmed_by')
                ).filter(n_confirmations = 1)
            s = _compose_text(teacher, attempts, template)
            print(s.encode('utf-8'))


