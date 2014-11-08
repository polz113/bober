from django.db import models
import bober_competition.models



# Create your models here.
class Submission(models.Model):
    user = models.ForeignKey(bober_competition.models.Users)
    text = models.TextField()
    comments = models.TextField()
    class_numeric = models.IntegerField()
    class_id = models.CharField(max_length=20)
