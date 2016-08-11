__author__ = 'Grega'
from django.db import models


class Category(models.Model):
    acronym = models.CharField(max_length=5)
    title = models.CharField(max_length=45)
    description = models.TextField()

    # For syncdb to work
    class Meta:
        app_label = 'application'