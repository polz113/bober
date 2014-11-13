from django.db import models
import bober_competition.models



# Create your models here.
class JuniorResult(models.Model):
    school_mentor = models.ForeignKey(bober_competition.models.CompetitionCategorySchoolMentor)
    drugi_razred = models.TextField()
    tretji_razred = models.TextField()
    cetrti_razred = models.TextField()
    peti_razred = models.TextField()
    pripombe = models.TextField()

