# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0029_auto_20151021_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('category', models.CharField(max_length=24, choices=[(b'ELEMENTARY', 'Elementary school'), (b'HIGHSCHOOL', 'High school'), (b'KINDERGARDEN', 'Kindergarden')])),
                ('address', models.CharField(max_length=1024, blank=True)),
                ('postal_code', models.IntegerField(null=True, blank=True)),
                ('post', models.CharField(max_length=255, blank=True)),
                ('tax_number', models.CharField(max_length=12, blank=True)),
                ('identifier', models.CharField(max_length=20, blank=True)),
                ('headmaster', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SchoolCategoryQuestionSets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_category', models.CharField(max_length=24, choices=[(b'ELEMENTARY', 'Elementary school'), (b'HIGHSCHOOL', 'High school'), (b'KINDERGARDEN', 'Kindergarden')])),
                ('competition', models.ForeignKey(to='bober_simple_competition.Competition')),
                ('questionsets', models.ManyToManyField(to='bober_simple_competition.CompetitionQuestionSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SchoolTeacherShortenedCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.ForeignKey(to='bober_si.School')),
                ('shortened_code', models.ForeignKey(to='bober_simple_competition.ShortenedCode')),
                ('teacher', models.ForeignKey(to='bober_simple_competition.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='schoolcategoryquestionsets',
            unique_together=set([('competition', 'school_category')]),
        ),
        migrations.CreateModel(
            name='SchoolCompetition',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('bober_simple_competition.competition',),
        ),
    ]
