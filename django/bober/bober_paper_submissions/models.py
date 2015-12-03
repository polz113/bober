#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.html import escape
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from code_based_auth.models import CodeField
from bober_simple_competition.models import Competition, Competitor, Profile, CompetitionQuestionSet, Attempt, AttemptConfirmation
from bober_si.models import School, SCHOOL_CATEGORIES, Award
import re

#DEFAULT_YEARS = {
#    u'1. razred': u'Jože Primer  10',
#    u'2. razred': u'Jana Novak 11',
#    u'3. razred': u'Tina Pobriši T. Primere 8',
#    u'2. razred': None,
#    u'3. razred': None,
#    u'4. razred': None,
#    u'5. razred': None,
#}

#DEFAULT_EXAMPLES = set(DEFAULT_YEARS.values())
#DEFAULT_EXAMPLES.remove(None)
# Create your models here.
class JuniorMentorship(models.Model):
    def __unicode__(self):
        return u"{}:{} - {}".format(self.teacher, self.school, self.competition.slug)
    competition = models.ForeignKey(Competition)
    school = models.ForeignKey(School)
    teacher = models.ForeignKey(Profile)


def parse_competitor_data(data):
    #if raw_data in DEFAULT_EXAMPLES:
    #    raise ValidationError(_('Remove the provided examples'), code='remove_examples')
    competitor_data = list()
    #re_rez = re.compile(r"(\d+\.?\s*)?(?P<name>([A-Za-zřéöčćžüšđČĆŽŠĐ]+[\s.-]+){1,4}"
    #            r"[A-Za-zřéöüčćžšđČĆŽŠĐ.]+)[\s;:-]*(?P<points>\d+)\s*")
    re_rez = re.compile(ur"(\d+\.?\s*)?(?P<name>([^\W\d_]+[\s.-]+){1,4}"
                ur"([^\W\d_]|.)+)[\s;:-]+(?P<points>\d+)\s*", re.UNICODE)
        # re_rez = re.compile(ur"(\d+\.?\s*)?(?P<name>[^\W\d_]*)(?P<points>.*)",re.UNICODE)
    seen_students = set()
    for line, rezultat in enumerate(data.split("\n")):
        rezultat = rezultat.strip()
        mo = re_rez.match(rezultat)
        if len(rezultat) < 1:
            continue
        try:
            split_name = mo.group("name").split()
            parts = len(split_name)
            first_name = " ".join(split_name[:parts/2])
            last_name = " ".join(split_name[parts/2:])
            points = int(mo.group("points"))
            competitor_data.append((first_name, last_name, points))
            assert (first_name.upper(), last_name.upper()) not in seen_students
            seen_students.add((first_name.upper(), last_name.upper()))
        except:
            raise ValidationError(
                _('Error in line %(line_no)d: %(line)s.'),
                code='error_parsing',
                params = {'line_no': line+1, 'line': escape(rezultat)}
            )
    return competitor_data


class JuniorYear(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.name, self.mentorship)
    class Meta:
        ordering = ['name']

    mentorship = models.ForeignKey(JuniorMentorship)
    access_code = CodeField()
    questionset = models.ForeignKey(CompetitionQuestionSet, null=True)
    name = models.CharField(max_length = 16)
    raw_data = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    attempts = models.ManyToManyField(Attempt, through='JuniorAttempt')
    
    def save_results(self, competitor_data=None):
        if competitor_data is None:
            competitor_data = parse_competitor_data(self.raw_data)
        j_attempts_by_name = {}
        j_attempts_by_line = list(self.juniorattempt_set.order_by(
            'line').all().prefetch_related(
                'attempt', 'attempt__competitor'
            ))
        for j_a in j_attempts_by_line:
            c = j_a.attempt.competitor
            j_attempts_by_name[(c.first_name.upper(), c.last_name.upper())] = j_a
        unrecognized_attempts = []
        still_here = set()
        for line_no, (first_name, last_name, points) in enumerate(competitor_data):
            j_a = j_attempts_by_name.get((first_name.upper(), last_name.upper()), None)
            if j_a is None:
                unrecognized_attempts.append((line_no, first_name, last_name, points))
            else:
                still_here.add(j_a.id)
                j_a.line = line_no
                # j_a.score = points
                j_a.attempt.score = points
                j_a.attempt.competitor.first_name = first_name
                j_a.attempt.competitor.last_name = last_name
                j_a.attempt.competitor.save()
                j_a.attempt.save()
                j_a.save()
        missing = []
        missing_ids = set()
        for j_a in j_attempts_by_line:
            if j_a.id not in still_here:
                missing.append(j_a)
                missing_ids.add(j_a.id)
        #print unrecognized_attempts
        #print "missing:", missing_ids
        for i, (line_no, first_name, last_name, points) in enumerate(unrecognized_attempts):
            if i < len(missing) and missing[i].attempt.score == points:
                j_a = missing[i]
                missing_ids.remove(j_a.id)
                a = j_a.attempt
                c = a.competitor
            else:
                c = Competitor()
                a = Attempt(competitionquestionset = self.questionset,
                    random_seed=0, access_code = 'Beavers bridging brooks')
                j_a = JuniorAttempt(year_class = self)
            c.first_name = first_name
            c.last_name = last_name
            c.save()
            a.score = points
            a.competitor = c
            a.save()
            j_a.line = line_no
            # j_a.score = points
            j_a.attempt = a
            # j_a.competitor = c
            j_a.save()
        #print "   still missing:", missing_ids
        for j_a in JuniorAttempt.objects.filter(id__in=missing_ids):
            j_a.attempt.competitor.delete()
            j_a.attempt.delete()
            j_a.delete()
        created_one = False
        my_attempts = list(Attempt.objects.filter(juniorattempt__year_class = self))
        for a in my_attempts:
            confirmation, created = AttemptConfirmation.objects.get_or_create(
                by=self.mentorship.teacher, attempt=a)
            created_one = created_one or created
        if created_one:
            # we should probably recreate the awards.
            pass

class JuniorDefaultYear(models.Model):
    competition = models.ForeignKey(Competition)
    school_category = models.CharField(choices=SCHOOL_CATEGORIES, max_length=24)
    questionset = models.ForeignKey(CompetitionQuestionSet)
    name = models.CharField(max_length = 16)
    value = models.TextField(blank=True, null=True)


class JuniorAttempt(models.Model):
    def __unicode__(self):
        return u"{}:{} {}".format(self.competitor, self.year_class, self.remarks)
    year_class = models.ForeignKey(JuniorYear)
    # competitor = models.ForeignKey(Competitor)
    attempt = models.OneToOneField(Attempt, null=True)
    line = models.IntegerField(default=-1)
    remarks = models.TextField(blank=True, null=True)
    # score = models.FloatField(null=True)

#class JuniorAward(models.Model):
#    award = models.ForeignKey(Award)
#    attempt = models.ForeignKey(JuniorAttempt)
#    note = models.CharField(max_length=1024, 
#        blank=True, default='')
#    serial = models.CharField(max_length=256, blank=True, default='')


def fill_mentorship_years(sender, instance=None, **kwargs):
    if instance:
        for default_year in JuniorDefaultYear.objects.filter(
                competition = instance.competition,
                school_category = instance.school.category):
            year, created = JuniorYear.objects.get_or_create(
                mentorship = instance,
                name = default_year.name)
            if created:
                year.raw_data = default_year.value
                year.save()

models.signals.post_save.connect(fill_mentorship_years, sender=JuniorMentorship)
