# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0044_auto_20151125_1700'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shortenedcode',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='shortenedcode',
            name='code',
        ),
        migrations.RemoveField(
            model_name='shortenedcode',
            name='competition_questionset',
        ),
        migrations.DeleteModel(
            name='ShortenedCode',
        ),
    ]
