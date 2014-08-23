__author__ = 'Grega'
from django.db import models

from application.models import *


class DifficultyLevel(models.Model):
    value = models.CharField(max_length=45)
    tasks = models.ManyToManyField("Task", through="AgeGroupTask")

    # For syncdb to work
    class Meta:
        app_label = 'application'