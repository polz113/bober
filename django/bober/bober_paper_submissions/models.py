#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from bober_simple_competition.models import Competition, Competitor, Profile
from bober_si.models import School

DEFAULT_YEARS = {
    u'1. razred': u'Jože Primer  10',
    u'2. razred': u'Jana Novak 11',
    u'3. razred': u'Tina Pobriši T. Primere 8',
    u'4. razred': None,
    u'5. razred': None,
}

DEFAULT_EXAMPLES = set(DEFAULT_YEARS.values())
DEFAULT_EXAMPLES.remove(None)
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

class JuniorAttempt(models.Model):
    def __unicode__(self):
        return u"{}:{} {}".format(self.competitor, self.year_class, self.remarks)
    year_class = models.ForeignKey(JuniorYear)
    competitor = models.ForeignKey(Competitor)
    remarks = models.TextField(blank=True)


def fill_mentorship_years(sender, instance=None, **kwargs):
    if instance:
        if instance.junioryear_set.count() < 1:
            for name, val in DEFAULT_YEARS.iteritems():
                # print "Creating", name
                year = JuniorYear(mentorship = instance, name=name)
                if val:
                    year.raw_data = val
                year.save()

models.signals.post_save.connect(fill_mentorship_years, sender=JuniorMentorship)
