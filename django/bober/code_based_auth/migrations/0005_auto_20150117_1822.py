# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0004_auto_20150104_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_algorithm',
            field=models.CharField(blank=True, max_length=16, null=True, choices=[(b'md5', b'md5'), (b'sha1', b'sha1'), (b'sha224', b'sha224'), (b'sha256', b'sha256'), (b'sha384', b'sha384'), (b'sha512', b'sha512'), (b'noop', b'No hash')]),
            preserve_default=True,
        ),
    ]
