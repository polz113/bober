# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import code_based_auth.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', code_based_auth.models.CodeField()),
                ('salt', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=64)),
                ('hash_format', models.CharField(max_length=2, choices=[(b'h', b'hex default'),
                                                                        (b'i', b'decimal default'),
                                                                        (b'w', b'words default'),
                                                                        (b'r', b'raw no hash'),
                                                                        (b'a', b'match any')])),
                ('hash_bits', models.PositiveIntegerField()),
                ('hash_algorithm', models.CharField(default=b'default', max_length=16)),
                ('max_parts', models.IntegerField(default=1)),
                ('part_separator', models.CharField(default=b'+', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeFormat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('separator', models.CharField(default=b'-', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeGenerator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_code_component', models.CharField(max_length=256, null=True, blank=True)),
                ('salt', models.CharField(max_length=256)),
                ('codes', models.ManyToManyField(to='code_based_auth.Code')),
                ('format', models.ForeignKey(to='code_based_auth.CodeFormat', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=256)),
                ('code', models.ForeignKey(related_name='parts', to='code_based_auth.Code',
                                           on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='codecomponent',
            name='code_format',
            field=models.ForeignKey(related_name='components', to='code_based_auth.CodeFormat',
                                    on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='format',
            field=models.ForeignKey(to='code_based_auth.CodeFormat', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
