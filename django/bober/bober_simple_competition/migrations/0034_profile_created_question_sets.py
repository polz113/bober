# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0033_auto_20151028_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_question_sets',
            field=models.ManyToManyField(related_name='creator_set', null=True, to='bober_simple_competition.QuestionSet', blank=True),
            preserve_default=True,
        ),
    ]
