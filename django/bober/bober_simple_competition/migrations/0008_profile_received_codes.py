# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0002_auto_20141227_1537'),
        ('bober_simple_competition', '0007_competitionquestionset_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='received_codes',
            field=models.ManyToManyField(related_name='user_set', null=True, to='code_based_auth.Code', blank=True),
            preserve_default=True,
        ),
    ]
