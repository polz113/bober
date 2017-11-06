# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0011_auto_20160913_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_algorithm',
            field=models.CharField(blank=True, max_length=16, null=True, choices=[(b'SHA1', b'SHA1'), (b'SHA224', b'SHA224'), (b'SHA', b'SHA'), (b'SHA384', b'SHA384'), (b'ecdsa-with-SHA1', b'ecdsa-with-SHA1'), (b'SHA256', b'SHA256'), (b'SHA512', b'SHA512'), (b'md4', b'md4'), (b'md5', b'md5'), (b'sha1', b'sha1'), (b'dsaWithSHA', b'dsaWithSHA'), (b'DSA-SHA', b'DSA-SHA'), (b'sha224', b'sha224'), (b'dsaEncryption', b'dsaEncryption'), (b'DSA', b'DSA'), (b'RIPEMD160', b'RIPEMD160'), (b'sha', b'sha'), (b'MD5', b'MD5'), (b'MD4', b'MD4'), (b'sha384', b'sha384'), (b'sha256', b'sha256'), (b'sha512', b'sha512'), (b'ripemd160', b'ripemd160'), (b'whirlpool', b'whirlpool'), (b'noop', 'No hash')]),
        ),
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_format',
            field=models.CharField(max_length=2, choices=[(b'h', 'hex'), (b'i', 'decimal'), (b'l', 'letters and digits'), (b'L', 'case-insensitive letters and digits'), (b's', 'unambiguous letters and digits'), (b'S', 'case-insensitive unambiguous letters and digits'), (b'w', 'words'), (b'W', 'case-insensitive words'), (b'r', 'raw no hash')]),
        ),
    ]
