# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0032_auto_20151025_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeeffect',
            name='effect',
            field=models.CharField(max_length=64, choices=[(b'let_manage', 'Allow the creator to manage the profile of anyone using this code'), (b'let_manage_recursive', 'Allow the creator and their managers to manage the profile of anyone using this code')]),
            preserve_default=True,
        ),
    ]
