# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codegenerator',
            name='codes',
            field=models.ManyToManyField(to=b'code_based_auth.Code', null=True, blank=True),
        ),
    ]
