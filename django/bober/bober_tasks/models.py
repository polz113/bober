import os
import json
import zipfile
import mimetypes
from io import StringIO
from bs4 import BeautifulSoup

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import django.template
from django.utils.text import slugify

import bober_simple_competition

TASK_TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'task_templates')
TASK_TEMPLATES = tuple([(i[:-len('.html')], i)
                        for i in os.listdir(TASK_TEMPLATE_DIR)
                        if i.endswith('.html')])


class AgeGroup(models.Model):
    value = models.CharField(max_length=45)
    tasks = models.ManyToManyField('Task', through='AgeGroupTask')


class AgeGroupTask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    age_group = models.ForeignKey('AgeGroup', on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE)


class Answer(models.Model):
    def __str__(self):
        return u"{}: {}({}, {}) - {}".format(
            self.task_translation.task,
            self.task_translation.title,
            self.task_translation.version,
            self.task_translation.language_locale,
            self.label)
        return self.international_id

    task_translation = models.ForeignKey('TaskTranslation', on_delete=models.CASCADE)
    value = models.TextField(null=True)
    label = models.CharField(max_length=8, blank=True, default='')
    correct = models.BooleanField(default=False)
    ordering = ['label']


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
    task_translation = models.ForeignKey('TaskTranslation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Resources(models.Model):
    def __str__(self):
        return u"{}: {}({}, {})".format(self.task,
                                        self.filename, self.type,
                                        self.language)

    filename = models.CharField(max_length=90)
    type = models.CharField(max_length=40)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    language = models.CharField(max_length=8, choices=settings.LANGUAGES)


class Task(models.Model):
    def __str__(self):
        return self.international_id

    international_id = models.CharField(max_length=16, unique=True)
    interaction_type = models.CharField(max_length=45,
                                        default='non-interactive')
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=5)
    categories = models.ManyToManyField("Category")
    age_groups = models.ManyToManyField("AgeGroup", through="AgeGroupTask")
    difficulty_levels = models.ManyToManyField("DifficultyLevel",
                                               through="AgeGroupTask")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=128, blank=True)

    def age_group_categories(self):
        return AgeGroupTask.objects.filter(task_id=self.id).all()

    def get_latest(self):
        return TaskTranslation.objects.filter(task=self).order_by('timestamp')[0]

    def get_latest_translation(self, language):
        return self.tasktranslation_set.filter(language_locale=language).latest('version')

    def available_languages(self):
        return self.tasktranslation_set.values_list(
            'language_locale', flat=True).distinct()


class TaskTranslation(models.Model):
    def __str__(self):
        return u"{}: {}({}, {})".format(self.task, self.title,
                                        self.version, self.language_locale)

    title = models.CharField(max_length=90)
    template = models.CharField(max_length=255, choices=TASK_TEMPLATES)
    body = models.TextField()
    solution = models.TextField()
    it_is_informatics = models.TextField(blank=True)
    language_locale = models.CharField(max_length=8, null=True, blank=True,
                                       choices=settings.LANGUAGES)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    version = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def correct_answer(self):
        try:
            return self.answer_set.filter(correct=True)[0]
        except Exception:
            # TODO: handle exception
            return None

    def save_new_version(self):
        task = self.task
        self.version = task.get_latest_translation(self.language_locale).version + 1
        answers = list(self.answer_set.all())
        self.id = None
        self.save()
        for a in answers:
            a.id = None
            a.task_translation = self
            a.save()

    def versions(self):
        return TaskTranslation.objects.filter(
            task=self.task,
            language_locale=self.language_locale).order_by("-version")

    @staticmethod
    def last_translation(task_id, language):
        return TaskTranslation.objects.filter(
            language_locale=language, task=task_id).order_by('timestamp')[0]

    def create_default_answers(self):
        if self.answer_set.count() > 0:
            return
        for i in "ABCD":
            a = Answer(label=i, task_translation=self)
            a.save()

    def render_to_string(self):
        with open(os.path.join(TASK_TEMPLATE_DIR, self.template) + '.html', 'r') as f:
            template = django.template.Template(f.read())
        d = dict()
        d['body'] = self.body
        d['answers'] = self.answer_set.all()
        d['title'] = self.title
        return template.render(django.template.Context(d))

    def render_solution_to_string(self):
        with open(os.path.join(TASK_TEMPLATE_DIR, 'api', 'solution.html'), 'r') as f:
            template = django.template.Template(f.read())
        d = dict()
        d['solution'] = self.solution
        d['it_is_informatics'] = self.it_is_informatics
        d['answers'] = self.answer_set.all()
        d['title'] = self.title
        return template.render(django.template.Context(d))

    def as_zip(self):
        authors = []
        translators = []
        if self.task.author is not None:
            authors = [self.task.author]
        if self.author is not None:
            translators = [self.author.first_name + u" " + self.author.last_name]
        manifest_dict = {
            "id": self.task.international_id,
            "interaction_type": 'non-interactive',
            "country": self.task.country,
            "authors": authors,
            "version": self.version,
            "title": self.title,
            "translators": translators,
            "license": "Creative commons CCBy",
            "browserSupport": [{"name": "ie", "version": 6, "os": "windows", "supported": False}],
            "acceptedAndsers": list(self.answer_set.filter(correct=True).values_list('value', flat=True)),
            "task": [{'type': 'html', 'url': 'index.html'}],
            "solution": [{"type": "html", "content": "solution.html"}],
            "task_modules": [{"type": "javascript", "url": "js/jquery.js"}],
            "grader_modules": [],
            "solution_modules": [{"type": "javascript", "url": "js/jquery.js"}],
            }
        resources = Resources.objects.filter(task=self.task,
                                             language=self.language_locale)
        # Check for specific task resources and add them to 'task' section
        # in Manifest.json (default resources are index.html and Functions.js)
        zip_stringio = StringIO.StringIO()
        zf = zipfile.ZipFile(zip_stringio, "w")
        for r in resources.all():
            f_path = os.path.join(
                settings.MEDIA_ROOT,
                'task',
                str(self.task_id),
                str(self.language_locale),
                'resources',
                r.filename)
            zf.write(f_path, 'resources/' + r.filename)
            manifest_dict['task'].append({
                'type': r.type,
                'url': 'resources/' + r.filename})
        # Generate Manifest.json, index.html, solution.html
        manifest = json.dumps(manifest_dict)
        solution_site = self.render_solution_to_string().encode('utf-8')
        index_site = self.render_to_string().encode('utf-8')
        zf.writestr('Manifest.json', manifest)
        zf.writestr('index.html', index_site)
        zf.writestr('solution.html', solution_site)
        zf.close()
        return zip_stringio.getvalue()

    def export_to_simple_competition(self, rebuild_caches=False):
        # if request.method == 'GET':
        #    return redirect("/")
        accepted_answers = self.answer_set.filter(correct=True)
        authors = []
        if self.task.author:
            try:
                authors.append(str(self.task.author))
            except Exception:
                # TODO: handle exception
                authors.append(str(self.task.author))
        if self.author:
            authors.append(u"%s" % self.author)
        q, created = bober_simple_competition.models.Question.objects.get_or_create(
            identifier=str(self.task.id))
        if created:
            q.slug = slugify(self.title) + '-' + str(self.task.id)
        else:
            q.resource_set.all().delete()
        q.country = self.task.country
        q.verification_function_type = 0  # non-interactive
        q.verification_function = u",".join([str(a.id) for a in accepted_answers])
        q.title = self.title
        q.version = self.version
        q.authors = ", ".join(authors)
        q.language = self.language_locale
        q.save()
        # print q, tt
        index_str = self.render_to_string()
        index_soup = BeautifulSoup(index_str, "lxml")
        # print index_str.encode('utf-8')
        # print resource_list
        index_resource = bober_simple_competition.models.Resource(
            question=q,
            relative_url='index.html',
            file=None,
            resource_type='html',
            mimetype='text/html',
            data=index_str.encode('utf-8'))
        index_resource.save()
        resource_list = bober_simple_competition.models._resource_list(index_soup)
        for d in resource_list:
            print(d['url'])
            try:
                resource = self.task.resources_set.filter(
                    language=self.language_locale,
                    filename=os.path.basename(d['url']))[0]
                f_path = os.path.join(
                    settings.MEDIA_ROOT,
                    'task',
                    str(self.task_id),
                    str(self.language_locale),
                    'resources',
                    resource.filename)
                with open(f_path, mode='rb') as f:
                    data = bytes(f.read())
                    r = bober_simple_competition.models.Resource(
                        question=q,
                        relative_url='resources/' + resource.filename,
                        resource_type=d['type'],
                        mimetype=mimetypes.guess_type(d['url'])[0],
                        file=None,
                    )
                    r.save()
                    r.data = data
                    r.save()
            except Exception as e:
                # TODO: handle exception
                pass
        if rebuild_caches:
            for qs in q.questionset_set.all():
                qs.rebuild_caches()


def create_default_answers(sender, instance=None, **kwargs):
    instance.create_default_answers()
