
__author__ = 'Grega'
from django.db import models
from application.models import *
from django.contrib.auth.models import User


class TaskTranslation(models.Model):
    title = models.CharField(max_length=90)
    body = models.TextField()
    solution = models.TextField()
    it_is_informatics = models.TextField( null=True)
    language_locale = models.ForeignKey('Language', null=True)
    task = models.ForeignKey('Task')
    author = models.ForeignKey(User, null = True)
    correct_answer = models.ForeignKey('Answer', null=True)
    comment = models.TextField( null=True)
    version = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def save_new_version(self):
        task = self.task
        self.version = task.get_latest_translation(self.language_locale).version + 1
        self.id = None
        self.save()

    @staticmethod
    def last_translation(task_id, language):
        return TaskTranslation.objects.filter(language_locale=language, task=task_id).order_by('timestamp')[0]

    # For syncdb to work
    class Meta:
        app_label = 'application'