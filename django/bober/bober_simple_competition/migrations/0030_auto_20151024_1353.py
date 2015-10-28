# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0029_auto_20151021_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortenedcode',
            old_name='competition_question_set',
            new_name='competition_questionset',
        ),
    ]
