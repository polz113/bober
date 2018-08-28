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
                ('code', models.ForeignKey(to='code_based_auth.Code', on_delete=models.CASCADE)),
                ('school', models.ForeignKey(to='bober_si.School', on_delete=models.CASCADE)),
                ('teacher', models.ForeignKey(to='bober_simple_competition.Profile', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        )
    ]
