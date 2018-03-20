# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-20 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0012_auto_20171104_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_algorithm',
            field=models.CharField(blank=True, choices=[('blake2s256', 'blake2s256'), ('sha384', 'sha384'), ('sha1', 'sha1'), ('sha256', 'sha256'), ('MD4', 'MD4'), ('SHA1', 'SHA1'), ('BLAKE2s256', 'BLAKE2s256'), ('SHA384', 'SHA384'), ('BLAKE2b512', 'BLAKE2b512'), ('SHA256', 'SHA256'), ('blake2b512', 'blake2b512'), ('RIPEMD160', 'RIPEMD160'), ('ripemd160', 'ripemd160'), ('md5', 'md5'), ('MD5-SHA1', 'MD5-SHA1'), ('SHA512', 'SHA512'), ('whirlpool', 'whirlpool'), ('sha224', 'sha224'), ('MD5', 'MD5'), ('sha512', 'sha512'), ('md5-sha1', 'md5-sha1'), ('SHA224', 'SHA224'), ('md4', 'md4'), ('noop', 'No hash')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_format',
            field=models.CharField(choices=[('h', 'hex'), ('i', 'decimal'), ('l', 'letters and digits'), ('L', 'case-insensitive letters and digits'), ('s', 'unambiguous letters and digits'), ('S', 'case-insensitive unambiguous letters and digits'), ('w', 'words'), ('W', 'case-insensitive words'), ('r', 'raw no hash')], max_length=2),
        ),
        migrations.AlterField(
            model_name='codecomponent',
            name='part_separator',
            field=models.CharField(default='+', max_length=1),
        ),
        migrations.AlterField(
            model_name='codeformat',
            name='separator',
            field=models.CharField(default='*', max_length=1),
        ),
    ]
