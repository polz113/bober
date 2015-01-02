# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0002_auto_20141227_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_algorithm',
            field=models.CharField(blank=True, max_length=16, null=True, choices=[(b'SHA1', b'SHA1'), (b'SHA224', b'SHA224'), (b'SHA', b'SHA'), (b'SHA384', b'SHA384'), (b'ecdsa-with-SHA1', b'ecdsa-with-SHA1'), (b'SHA256', b'SHA256'), (b'SHA512', b'SHA512'), (b'md4', b'md4'), (b'md5', b'md5'), (b'sha1', b'sha1'), (b'dsaWithSHA', b'dsaWithSHA'), (b'DSA-SHA', b'DSA-SHA'), (b'sha224', b'sha224'), (b'dsaEncryption', b'dsaEncryption'), (b'DSA', b'DSA'), (b'RIPEMD160', b'RIPEMD160'), (b'sha', b'sha'), (b'MD5', b'MD5'), (b'MD4', b'MD4'), (b'sha384', b'sha384'), (b'sha256', b'sha256'), (b'sha512', b'sha512'), (b'ripemd160', b'ripemd160'), (b'whirlpool', b'whirlpool')]),
        ),
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_format',
            field=models.CharField(max_length=2, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'w', b'words'), (b'r', b'raw no hash'), (b'a', b'match any')]),
        ),
    ]
