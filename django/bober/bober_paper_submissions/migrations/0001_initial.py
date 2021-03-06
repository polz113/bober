# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 10:07
from __future__ import unicode_literals

import code_based_auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bober_simple_competition', '0052_auto_20160921_1007'),
        ('bober_si', '0004_auto_20160913_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuniorAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.IntegerField(default=-1)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('attempt', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bober_simple_competition.Attempt')),
            ],
        ),
        migrations.CreateModel(
            name='JuniorDefaultYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_category', models.CharField(choices=[(b'ELEMENTARY', 'Elementary school'), (b'HIGHSCHOOL', 'High school'), (b'KINDERGARDEN', 'Kindergarden')], max_length=24)),
                ('name', models.CharField(max_length=16)),
                ('value', models.TextField(blank=True, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_simple_competition.Competition')),
                ('questionset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_simple_competition.CompetitionQuestionSet')),
            ],
        ),
        migrations.CreateModel(
            name='JuniorMentorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_simple_competition.Competition')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_si.School')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_simple_competition.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='JuniorYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_code', code_based_auth.models.CodeField()),
                ('name', models.CharField(max_length=16)),
                ('raw_data', models.TextField(blank=True)),
                ('remarks', models.TextField(blank=True)),
                ('attempts', models.ManyToManyField(through='bober_paper_submissions.JuniorAttempt', to='bober_simple_competition.Attempt')),
                ('mentorship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_paper_submissions.JuniorMentorship')),
                ('questionset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bober_simple_competition.CompetitionQuestionSet')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='juniorattempt',
            name='year_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bober_paper_submissions.JuniorYear'),
        ),
    ]
