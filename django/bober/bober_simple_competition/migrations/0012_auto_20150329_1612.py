# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0011_auto_20150328_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='guest_code',
            field=models.ForeignKey(blank=True, to='code_based_auth.Code',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
