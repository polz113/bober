__author__ = 'Gregor Pompe'
from django.db import models
from django.conf import settings
from django.db.models import Max
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class AgeGroup(models.Model):
    value = models.CharField(max_length=45)
    tasks = models.ManyToManyField('Task', through='AgeGroupTask')

class AgeGroupTask(models.Model):
    task = models.ForeignKey('Task')
    age_group = models.ForeignKey('AgeGroup')
    difficulty_level = models.ForeignKey('DifficultyLevel')

class Answer(models.Model):
    task_translation = models.ForeignKey('TaskTranslation')
    value = models.TextField(null=True)

class Category(models.Model):
    acronym = models.CharField(max_length=5)
    title = models.CharField(max_length=45)
    description = models.TextField()

class DifficultyLevel(models.Model):
    value = models.CharField(max_length=45)
    tasks = models.ManyToManyField("Task", through="AgeGroupTask")

class Remark(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    task_translation = models.ForeignKey('TaskTranslation')
    user = models.ForeignKey(User)

class Resources(models.Model):
    filename = models.CharField(max_length=90)
    type = models.CharField(max_length=40)
    task = models.ForeignKey('Task')
    language = models.CharField(max_length = 8, choices=settings.LANGUAGES)

class Task(models.Model):
    international_id = models.CharField(max_length=16)
    interaction_type = models.CharField(max_length=45)
    parent = models.ForeignKey("self", null = True)
    categories = models.ManyToManyField("Category")
    age_groups = models.ManyToManyField("AgeGroup", through="AgeGroupTask")
    difficulty_levels = models.ManyToManyField("DifficultyLevel", through="AgeGroupTask")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, null = True)

    def age_group_categories(self):
        return AgeGroupTask.objects.filter(task_id = self.id).all()

    def get_latest(self):
        return TaskTranslation.objects.filter(task=self).order_by('timestamp')[0]

    def get_latest_translation(self, language):
        return self.tasktranslation_set.filter(language_locale=language).latest('version')

    def available_languages(self):
        languages = {}
        for translation in self.tasktranslation_set.all():
            languages[translation.language_locale] = 1
        return languages.keys()

class TaskTranslation(models.Model):
    title = models.CharField(max_length=90)
    body = models.TextField()
    solution = models.TextField()
    it_is_informatics = models.TextField(blank=True)
    language_locale = models.CharField(max_length=8, null=True, blank=True,
                                        choices=settings.LANGUAGES)
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

