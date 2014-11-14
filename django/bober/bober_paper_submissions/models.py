from django.db import models
import bober_competition.models



# Create your models here.
class JuniorResult(models.Model):
    def __unicode__(self):
        return u"{}:{} {}".format(self.id, self.school_mentor, self.pripombe)
    school_mentor = models.ForeignKey(bober_competition.models.CompetitionCategorySchoolMentor)
    drugi_razred = models.TextField(blank=True)
    tretji_razred = models.TextField(blank=True)
    cetrti_razred = models.TextField(blank=True)
    peti_razred = models.TextField(blank=True)
    pripombe = models.TextField(blank=True)

