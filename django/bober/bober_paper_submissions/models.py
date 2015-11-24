#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from bober_simple_competition.models import Competition, Competitor, Profile
from bober_si.models import School, SCHOOL_CATEGORIES
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
                _('Error in line %(line)d.'),
                code='error_parsing',
                params = {'line': line+1}
            )
    return competitor_data

class JuniorYear(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.name, self.mentorship)
    class Meta:
        ordering = ['name']
    mentorship = models.ForeignKey(JuniorMentorship)
    name = models.CharField(max_length = 16)
    raw_data = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    
    def save_results(self, competitor_data=None):
        if competitor_data is None:
            competitor_data = parse_competitor_data(self.raw_data)
        still_here = list()
        for first_name, last_name, points in competitor_data:
            c, created = Competitor.objects.get_or_create(
                first_name = first_name,
                last_name = last_name,
                juniorattempt__year_class = self)
            if not created:
                c.juniorattempt_set.all().delete()
            c.first_name = first_name
            c.last_name = last_name
            c.save()
            still_here.append(c.id)
            a = JuniorAttempt(year_class = self, competitor = c, score=points)
            a.save()
        Competitor.objects.filter(
            juniorattempt__year_class = self,
            profile=None).exclude(id__in=still_here).delete() 

class JuniorDefaultYear(models.Model):
    competition = models.ForeignKey(Competition)
    school_category = models.CharField(choices=SCHOOL_CATEGORIES, max_length=24)
    name = models.CharField(max_length = 16)
    value = models.TextField(blank=True, null=True)

class JuniorAttempt(models.Model):
    def __unicode__(self):
        return u"{}:{} {}".format(self.competitor, self.year_class, self.remarks)
    year_class = models.ForeignKey(JuniorYear)
    competitor = models.ForeignKey(Competitor)
    remarks = models.TextField(blank=True)
    score = models.FloatField(null=True)

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
