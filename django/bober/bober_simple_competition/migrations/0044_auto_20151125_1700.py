# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0043_attempt_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_codes',
            field=models.ManyToManyField(related_name='creator_set', to='code_based_auth.Code', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_question_sets',
            field=models.ManyToManyField(related_name='creator_set', to='bober_simple_competition.QuestionSet', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='managed_profiles',
            field=models.ManyToManyField(related_name='managers', to='bober_simple_competition.Profile', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='question_sets',
            field=models.ManyToManyField(to='bober_simple_competition.QuestionSet', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='questions',
            field=models.ManyToManyField(to='bober_simple_competition.Question', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='received_codes',
            field=models.ManyToManyField(related_name='recipient_set', to='code_based_auth.Code', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='used_codes',
            field=models.ManyToManyField(related_name='user_set', to='code_based_auth.Code', blank=True),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='resource_caches',
            field=models.ManyToManyField(to='bober_simple_competition.ResourceCache', blank=True),
        ),
    ]
