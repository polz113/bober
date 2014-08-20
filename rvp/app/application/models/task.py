import datetime

__author__ = 'Grega'
from django.db import models

from application.models import *
from django.contrib.auth.models import User

class Task(models.Model):
    international_id = models.CharField(max_length=16)
    interaction_type = models.CharField(max_length=45)
    parent = models.ForeignKey("self", null = True)
    categories = models.ManyToManyField("Category")
    age_groups = models.ManyToManyField("AgeGroup", through="AgeGroupTask")
    difficulty_levels = models.ManyToManyField("DifficultyLevel", through="AgeGroupTask")
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now, auto_now = True)
    author = models.ForeignKey(User, null = True)

    def age_group_categories(self):
        return AgeGroupTask.objects.filter(task_id = self.id).all()

    def get_latest(self):
        return TaskTranslation.objects.filter(task=self).order_by('timestamp')[0]

    def get_latest_translation(self, language):
        return self.tasktranslation_set.filter(language_locale_id=language).latest('version')

    def available_languages(self):
        languages = {}
        for translation in self.tasktranslation_set.all():
            languages[translation.language_locale] = 1
        return languages.keys()
    # For syncdb to work
    class Meta:
        app_label = 'application'
