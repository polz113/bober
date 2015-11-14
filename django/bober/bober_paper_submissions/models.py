#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from bober_simple_competition.models import Competition, Competitor, Profile
from bober_si.models import School, SCHOOL_CATEGORIES

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

class JuniorYear(models.Model):
    def __unicode__(self):
        return u"{}: {}".format(self.name, self.mentorship)
    class Meta:
        ordering = ['name']
    mentorship = models.ForeignKey(JuniorMentorship)
    name = models.CharField(max_length = 16)
    raw_data = models.TextField(blank=True)
    remarks = models.TextField(blank=True)

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
