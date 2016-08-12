__author__ = 'Grega'
from django.db import models
from application.models import *


class AgeGroupTask(models.Model):
    task = models.ForeignKey('Task')
    age_group = models.ForeignKey('AgeGroup')
    difficulty_level = models.ForeignKey('DifficultyLevel')

    # For syncdb to work
    class Meta:
        app_label = 'application'