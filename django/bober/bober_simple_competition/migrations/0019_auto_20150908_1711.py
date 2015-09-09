# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0018_remove_profile_managed_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='question_sets',
            field=models.ManyToManyField(to='bober_simple_competition.QuestionSet', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionset',
            name='resource_caches',
            field=models.ManyToManyField(to='bober_simple_competition.ResourceCache', null=True, blank=True),
            preserve_default=True,
        ),
    ]
