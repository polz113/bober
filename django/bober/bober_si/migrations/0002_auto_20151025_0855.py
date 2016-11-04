# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_based_auth', '0010_auto_20151025_0823'),
        ('bober_simple_competition', '0032_auto_20151025_0848'),
        ('bober_si', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolTeacherCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.ForeignKey(to='code_based_auth.Code')),
                ('school', models.ForeignKey(to='bober_si.School')),
                ('teacher', models.ForeignKey(to='bober_simple_competition.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        #migrations.RemoveField(
        #    model_name='schoolteachershortenedcode',
        #    name='school',
        #),
        #migrations.RemoveField(
        #    model_name='schoolteachershortenedcode',
        #    name='shortened_code',
        #),
        #migrations.RemoveField(
        #    model_name='schoolteachershortenedcode',
        #    name='teacher',
        #),
        #migrations.DeleteModel(
        #    name='SchoolTeacherShortenedCode',
        #),
    ]
