# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-13 10:08
from __future__ import unicode_literals

import code_based_auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0013_auto_20180320_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeRevocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', code_based_auth.models.CodeField(db_index=True)),
                ('salt', models.CharField(max_length=256)),
                ('time', models.DateTimeField()),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='code_based_auth.Code')),
            ],
        ),
        migrations.AlterField(
            model_name='codecomponent',
            name='hash_algorithm',
            field=models.CharField(blank=True, choices=[('md4', 'md4'), ('sha512', 'sha512'), ('blake2b512', 'blake2b512'), ('sha224', 'sha224'), ('sha3_384', 'sha3_384'), ('blake2s256', 'blake2s256'), ('sha3-512', 'sha3-512'), ('sha384', 'sha384'), ('sha3_256', 'sha3_256'), ('sha512-256', 'sha512-256'), ('sha1', 'sha1'), ('md5', 'md5'), ('shake256', 'shake256'), ('sha3-224', 'sha3-224'), ('sha3-384', 'sha3-384'), ('shake_128', 'shake_128'), ('sha512-224', 'sha512-224'), ('blake2s', 'blake2s'), ('md5-sha1', 'md5-sha1'), ('shake128', 'shake128'), ('sha3_512', 'sha3_512'), ('shake_256', 'shake_256'), ('whirlpool', 'whirlpool'), ('sha256', 'sha256'), ('sha3_224', 'sha3_224'), ('sm3', 'sm3'), ('blake2b', 'blake2b'), ('ripemd160', 'ripemd160'), ('sha3-256', 'sha3-256'), ('noop', 'No hash')], max_length=16, null=True),
        ),
    ]
