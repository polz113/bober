__author__ = 'Grega'
from django.db import models
from task_translation import TaskTranslation
from django.contrib.auth.models import User

class Remark(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    task_translation = models.ForeignKey('TaskTranslation')
    user = models.ForeignKey(User)

    # For syncdb to work
    class Meta:
        app_label = 'application'