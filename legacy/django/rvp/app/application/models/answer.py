__author__ = 'Grega'
from django.db import models
from application.models import *


class Answer(models.Model):
    task_translation = models.ForeignKey('TaskTranslation')
    value = models.TextField(null=True)

    # For syncdb to work
    class Meta:
        app_label = 'application'