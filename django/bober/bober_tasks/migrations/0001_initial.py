# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AgeGroupTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_group', models.ForeignKey(to='bober_tasks.AgeGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField(null=True)),
                ('label', models.CharField(default=b'', max_length=8, blank=True)),
                ('correct', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acronym', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=8, choices=[(b'sl', 'Slovenian')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('international_id', models.CharField(max_length=16)),
                ('interaction_type', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=128, blank=True)),
                ('age_groups', models.ManyToManyField(to='bober_tasks.AgeGroup', through='bober_tasks.AgeGroupTask')),
                ('categories', models.ManyToManyField(to='bober_tasks.Category')),
                ('difficulty_levels', models.ManyToManyField(to='bober_tasks.DifficultyLevel', through='bober_tasks.AgeGroupTask')),
                ('parent', models.ForeignKey(to='bober_tasks.Task', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('solution', models.TextField()),
                ('it_is_informatics', models.TextField(blank=True)),
                ('language_locale', models.CharField(blank=True, max_length=8, null=True, choices=[(b'sl', 'Slovenian')])),
                ('comment', models.TextField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('correct_answer', models.ForeignKey(to='bober_tasks.Answer', null=True)),
                ('task', models.ForeignKey(to='bober_tasks.Task')),
                ('translator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='resources',
            name='task',
            field=models.ForeignKey(to='bober_tasks.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='remark',
            name='task_translation',
            field=models.ForeignKey(to='bober_tasks.TaskTranslation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='remark',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='tasks',
            field=models.ManyToManyField(to='bober_tasks.Task', through='bober_tasks.AgeGroupTask'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='task_translation',
            field=models.ForeignKey(to='bober_tasks.TaskTranslation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agegrouptask',
            name='difficulty_level',
            field=models.ForeignKey(to='bober_tasks.DifficultyLevel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agegrouptask',
            name='task',
            field=models.ForeignKey(to='bober_tasks.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agegroup',
            name='tasks',
            field=models.ManyToManyField(to='bober_tasks.Task', through='bober_tasks.AgeGroupTask'),
            preserve_default=True,
        ),
    ]
