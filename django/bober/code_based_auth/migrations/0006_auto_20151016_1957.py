# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0005_auto_20150117_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_format',
            field=models.CharField(max_length=2, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'w', b'words'), (b'r', b'raw no hash'), (b'a', b'match exact')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='codeformat',
            name='separator',
            field=models.CharField(default=b'*', max_length=1),
            preserve_default=True,
        ),
    ]
