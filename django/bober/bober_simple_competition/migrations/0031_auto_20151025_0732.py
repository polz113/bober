# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0008_auto_20151025_0732'),
        ('bober_simple_competition', '0030_auto_20151024_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('effect', models.CharField(max_length=64, choices=[(b'let_manage', 'Allow the creator to manage the profile of anyone using this code'), (b'let_invalidate', 'Allow the creator to invalidate any attempt using this code'), (b'let_manage_recursive', 'Allow the creator and their managers to manage the profile of anyone using this code')])),
                ('code', models.ForeignKey(to='code_based_auth.Code', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='competition',
            name='shortened_code_hash_format',
            field=models.CharField(default=b'h', max_length=2, null=True, blank=True, choices=[(b'h', b'hex'), (b'i', b'decimal'), (b'l', b'letters and digits'), (b'L', b'case-insensitive letters and digits'), (b'w', b'words'), (b'W', b'case-insensitive words'), (b'r', b'raw no hash')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shortenedcode',
            name='code',
            field=models.ForeignKey(to='code_based_auth.Code', unique=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='shortenedcode',
            unique_together=set([('competition_questionset', 'short')]),
        ),
    ]
