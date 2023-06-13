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

def create_si_national_awards(cqs):
    # print ("creating for", cqs)
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
    l = list(Attempt.objects.filter(
        competitionquestionset = cqs
    ).exclude(
        confirmed_by = None
    ).order_by('-score').values_list('score', flat=True))
    first_place_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'prva',
        defaults = {
            'threshold': None,
            'min_threshold': 0.0,
            'from_place': 1,
            'to_place': 1,
            'icon': 'prva.png',
            'template': 'prva',
            'serial_prefix': year_str + group_prefix + '1',
        }
    )
    second_place_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'druga',
        defaults = {
            'threshold': None,
            'min_threshold': 0.0,
            'from_place': 2,
            'to_place': 2,
            'template': 'druga',
            'icon': 'druga.png',
            'serial_prefix': year_str + group_prefix + '2',
        }
    )
    third_place_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'tretja',
        defaults = {
            'threshold': None,
            'min_threshold': 0.0,
            'from_place': 3,
            'to_place': 3,
            'icon': 'tretja.png',
            'template': 'tretja',
            'serial_prefix': year_str + group_prefix + '3',
        }
    )
    gold_award, gold_created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'zlato',
        defaults = {
            'threshold': None,
            'min_threshold': 0.0,
            'icon': 'zlato.png',
            'template': 'zlato',
            'serial_prefix': year_str + group_prefix + 'G',
        }
    )
    # print (cqs, l)
    if len(l) < 1:
        return
    silver_defaults = {
        'threshold': l[(len(l)-1)//2],
        'min_threshold': 0.0,
        'icon': 'srebrno.png',
        'template': 'srebrno',
        'serial_prefix': year_str + group_prefix + 'S',
    }
    if gold_award.to_place is not None:
        silver_defaults['from_place'] = gold_award.to_place+1
    silver_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'srebrno',
        defaults = silver_defaults
    )
    gold_award.replaces.add(silver_award)
    try:
        bronze_award = Award.objects.get(
            questionset = cqs,
            name = 'bronasto')
        silver_award.replaces.add(bronze_award)
        gold_award.replaces.add(bronze_award)
    except:
        pass
    try:
        general_award = Award.objects.get(
            questionset = cqs,
            name = 'priznanje')
        silver_award.replaces.add(general_award)
        gold_award.replaces.add(general_award)
    except:
        pass


def create_si_awards(cqs):
    # self.stdout.write("creating for {}".format(cqs))
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
    if max_score is None:
        max_score = 10
    bronze_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'bronasto',
        defaults = {
            'template': 'bronasto',
            'threshold': max_score,
            'icon': 'bronasto.png',
            'min_threshold': max_score // 2,
            'serial_prefix': year_str + group_prefix + 'B',
        }
    )
    if created or True:
        # set the threshold to cover 1/5 of all competitors
        l = Attempt.objects.filter(
                competitionquestionset = cqs
            ).exclude(
                confirmed_by = None
            ).order_by('-score').values_list('score', flat=True)
        # self.stdout.write("{}: {}".format(bronze_award, l))
        bronze_award.threshold = l[(len(l) - 1) // 5]
        bronze_award.save()
        # self.stdout.write("Created bronze {}".format(bronze_award))
    general_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'priznanje',
        defaults = {
            'threshold': 0,
            'template': 'priznanje',
            'min_threshold': 0.0,        
            'serial_prefix': year_str + group_prefix + 'P'
        },
    )
    bronze_award.replaces.add(general_award)
    promoted_award, created = Award.objects.get_or_create(
        questionset = cqs,
        group_name = group_name,
        name = 'napreduje',
        defaults = {
            'threshold': max_score,
            'icon': 'napreduje.png',
            'min_threshold': max_score,
            'serial_prefix': year_str + group_prefix + 'N',
        }
    )
    

# Teacher awards

DEFAULT_TEACHER_TEXT_TEMPLATE = (
    u"""{name} je bil(a) na tekmovanju Bober, ki je potekalo {time_string}, mentor(ica)
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

GENERIC_TEACHER_TEXT_TEMPLATES = {
    "solsko-.*": (
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
        }
    ),
    "drzavno-.*": (
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
        }
    )
    
}

TEACHER_TEXT_TEMPLATES = {
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


def _generic_text_template(cslug):
    for k, v in GENERIC_TEACHER_TEXT_TEMPLATES.items():
        if re.match(k, cslug):
            return v
    return DEFAULT_TEACHER_TEXT_TEMPLATE



def _competition_time_string(competition):
    start = competition.start.date()
    end = competition.end.date()
    months = [None, 'januarjem', 'februarjem', 'marcem', 'aprilom', 'majem', 'junijem',
              'julijem', 'avgustom', 'septembrom', 'oktobrom', 'novembrom', 'decembrom']
    months_n = [None, 'januarja', 'februarja', 'marca', 'aprila', 'maja', 'junija',
              'julija', 'avgusta', 'septembra', 'oktobra', 'novembra', 'decembra']
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
        res = "{}. {} {}".format(end.day, months_n[end.month], end.year)
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

def create_teacher_awards(competition):
    template = TEACHER_TEXT_TEMPLATES.get(
        cslug,
        _generic_text_template(cslug))
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
        # print("----------------------------")
        # print(teacher, teacher.user.email)
        # print("----------------------------")
        attempts = Attempt.objects.filter(
                competitionquestionset__competition = competition, 
                confirmed_by=teacher
            ).distinct()
        if False:
            # consider only attempts confirmed only by the mentor
            attempts = attempts.annotate(
                n_confirmations = Count('confirmed_by')
            ).filter(n_confirmations = 1)
        if attempts.count() > 0:
            s = _compose_text(competition, teacher, attempts, template)
            name_str = u"{} {}".format(
                teacher.user.first_name, teacher.user.last_name)
            if teacher.date_of_birth is not None:
                name_str += u", roj. {},".format(
                    teacher.date_of_birth.strftime('%d. %m. %Y'))
            # the serial under here is WRONG
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
                    # print("Updating")
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

