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

DEFAULT_TEXT_TEMPLATE = (u"""{name} je bil(a) na tekmovanju Bober, ki je potekalo {time_string}, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""", 
    {
        "m": u"""{name} je bil na tekmovanju Bober, ki je potekalo {time_string}, mentor
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        "f": u"""{name} je bila na tekmovanju Bober, ki je potekalo {time_string}, mentorica
{n_confirmed}.
{next_round_listing}
{award_listing}
"""
    }
)

TEXT_TEMPLATES = {
    "solsko-2016": (
        u"""je bil(a) na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo med 7. in 11. novembrom 2016, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""", 
        { 
            "m": None,
            "f": None
        }),
    "drzavno-2016": (
        u"""je bil(a) na državnem nivoju mednarodnega tekmovanja
Bober, ki je potekalo 14. 1. 2017, mentor(ica) 
{n_confirmed}.
{award_listing}
{top_places_listing}
""",
        { 
            "m": None,
            "f": None
        }),
    "drzavno2015": (
        u"""je bil(a) na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        { 
            "m": u"""je bil na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
            "f": u"""je bila na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentorica
{n_confirmed}.
{next_round_listing}
{award_listing}
"""
        }),
    "finale2015": (
        u"""je bil(a) na državnem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        { 
            "m": u"""je bil na državnem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
            "f": u"""je bila na državnem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentorica
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        }),
    "solsko-2017": (
        u"""je bil(a) na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        { 
            "m": u"""je bil na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
            "f": u"""je bila na šolskem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentorica
{n_confirmed}.
{next_round_listing}
{award_listing}
"""
        }),
    "drzavno-2017": (
        u"""je bil(a) na državnem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor(ica)
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        { 
            "m": u"""je bil na državnem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentor
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
            "f": u"""je bila na državnem nivoju mednarodnega tekmovanja 
Bober, ki je potekalo {competition_time}, mentorica
{n_confirmed}.
{next_round_listing}
{award_listing}
""",
        }),
 
}


def _competition_time_string(competition):
    start = competition.start.date()
    end = competition.end.date()
    months = [None, 'januarjem', 'februarjem', 'marcem', 'aprilom', 'majem', 'junijem',
              'julijem', 'avgustom', 'septembrom', 'oktobrom', 'novembrom', 'decembrom']
    if start.year != end.year:
        res = "med {}. {} {} in {}. {} {}".format(
            start.day, months[start.month], start.year,
            end.day, months[end.month], end.year)
    elif start.month != end.month:
        res = "med {}. {} in {}. {} {}".format(start.day, months[start.month],
            end.day, months[end.month], end.year)
    elif start.day != end.day:
        res = "med {}. in {}. {} {}".format(start.day,
            end.day, months[end.month], end.year)
    else:
        res = "{}. {} {}".format(end.day, months[end.month], end.year)
    return res


def _compose_text(competition, teacher, attempts, template):
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
    p_je = Plural(u"je", u"sta", u"so", u"jih je")
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
    if teacher.date_of_birth:
        name += u', roj. {},'.format(str(teacher.date_of_birth))
    template = template[1].get(teacher.gender, template[0])
    competition_time = _competition_time_string(competition)
    return template.format(**locals())

class Command(BaseCommand):
    # @transaction.atomic
    help = "Create the teacher certificates for a slovenian competition"

    def make_manifest(dirname):
        pass
        # print "haha"

    def add_arguments(self, parser):
        parser.add_argument('competition_slug', nargs=1)

    def __create_awards(self, cqs):
        pass

    def handle(self, *args, **options):
        if len(args) < 1:
            args += (None,) * (3 - len(args))
        cslug = options.get('competition_slug', [args[0]])[0]
        competition = SchoolCompetition.objects.get(slug=cslug)
        template = TEXT_TEMPLATES.get(cslug, DEFAULT_TEXT_TEMPLATE)
        default_recognition, created = \
            CompetitionRecognition.objects.get_or_create(
                competition = competition,
                template = 'potrdilo',
                defaults = {'serial_prefix' : 't-' + cslug}
            )
        organizer = competition.administrator_code_generator.codes.filter(
                code_parts__name='admin_privileges', 
                code_parts__value='view_all_admin_codes'
            )[0].creator_set.all()[0]
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
            if attempts.count():
                s = _compose_text(competition, teacher, attempts, template)
                name_str = u"{} {}".format(
                    teacher.user.first_name, teacher.user.last_name)
                if teacher.date_of_birth is not None:
                    name_str += u", roj. {},".format(
                        teacher.date_of_birth.strftime('%d. %m. %Y'))
                teacher_recognition, created = TeacherRecognition.objects.get_or_create(
                    template = default_recognition,
                    teacher = teacher,
                    revoked_by = None,
                    defaults = {
                        "recipient": name_str,
                        "text": s,
                        "serial": u"{}{}-0".format(
                            default_recognition.serial_prefix,
                            teacher.id)
                    })
                if not created:
                    if teacher_recognition.recipient != name_str or \
                                teacher_recognition.text != s:
                        print("Updating")
                        teacher_recognition.revoked_by = organizer
                        teacher_recognition.save()
                        try:
                            i = int(s.split('-')[-1]) +1
                        except ValueError:
                            i = 0
                        serial = u"{}{}-{}".format(
                                    default_recognition.serial_prefix,
                                    teacher.id, i)
                        while TeacherRecognition.objects.filter(
                                serial = serial).count():
                            i += 1
                            serial = u"{}{}-{}".format(
                                    default_recognition.serial_prefix,
                                    teacher.id, i)
                        new_teacher_recognition = \
                            TeacherRecognition.objects.get_or_create(
                                template = default_recognition,
                                teacher = teacher,
                                revoked_by = None,
                                recipient = name_str,
                                text = s,
                                serial = serial)
                teacher_recognition.save()


