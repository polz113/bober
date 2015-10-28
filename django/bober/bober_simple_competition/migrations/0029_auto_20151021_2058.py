# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0028_profile_feature_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='shortened_code_hash_algorithm',
            field=models.CharField(default=b'sha512', max_length=16, null=True, blank=True, choices=[(b'md5', b'md5'), (b'sha1', b'sha1'), (b'sha224', b'sha224'), (b'sha256', b'sha256'), (b'sha384', b'sha384'), (b'sha512', b'sha512'), (b'noop', b'No hash')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='shortened_code_hash_format',
            field=models.CharField(default=b'h', max_length=2, null=True, blank=True, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'l', b'letters and digits'), (b'L', b'case-insensitive letters and digits'), (b'w', b'words'), (b'W', b'case-insensitive words'), (b'r', b'raw no hash'), (b'a', b'match exact')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shortenedcode',
            name='short',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
    ]
