# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0006_auto_20151016_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_format',
            field=models.CharField(max_length=2, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'l', b'letters and digits'), (b'L', b'case-insensitive letters and digits'), (b'w', b'words'), (b'W', b'case-insensitive words'), (b'r', b'raw no hash'), (b'a', b'match exact')]),
            preserve_default=True,
        ),
    ]
