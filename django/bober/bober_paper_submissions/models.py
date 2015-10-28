from django.db import models
from bober_simple_competition.models import Competition, Profile
from bober_si.models import School


# Create your models here.
class JuniorMentorship(models.Model):
    competition = models.ForeignKey(Competition)
    school = models.ForeignKey(School)
    mentor = models.ForeignKey(Profile)

class JuniorYearClass(models.Model):
    mentorship = models.ForeignKey(JuniorMentorship)
    year = models.PositiveIntegerField()
    name = models.CharField(max_length = 2)
    remarks = models.TextField(blank=True)

class JuniorResult(models.Model):
    def __unicode__(self):
        return u"{}:{} {}".format(self.id, self.school_mentor, self.pripombe)
    year_class = models.ForeignKey(JuniorYearClass)
    first_name = models.CharField(max_length = 256)    
    last_name = models.CharField(max_length = 256)    
    remarks = models.TextField(blank=True)

