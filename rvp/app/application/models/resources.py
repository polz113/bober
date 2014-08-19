__author__ = 'Grega'
from django.db import models
from application.models import *


class Resources(models.Model):
    filename = models.CharField(max_length=90)
    type = models.CharField(max_length=40)
    task = models.ForeignKey('Task')
    language = models.ForeignKey('Language')

    # For syncdb to work
    class Meta:
        app_label = 'application'