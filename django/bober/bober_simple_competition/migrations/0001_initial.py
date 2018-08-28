# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import code_based_auth.models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('code_based_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('randomized_question_id', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_code', code_based_auth.models.CodeField()),
                ('random_seed', models.IntegerField()),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('finish', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('administrator_code_generator', models.ForeignKey(related_name='administrator_code_competition_set',
                                                                   to='code_based_auth.CodeGenerator',
                                                                   on_delete=models.CASCADE)),
                ('competitor_code_generator', models.ForeignKey(related_name='competitor_code_competition_set',
                                                                to='code_based_auth.CodeGenerator',
                                                                on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompetitionQuestionSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competition', models.ForeignKey(to='bober_simple_competition.Competition', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_code', code_based_auth.models.CodeField(null=True, blank=True)),
                ('vcard', models.TextField()),
                ('created_codes', models.ManyToManyField(related_name='owner_set', null=True, to='code_based_auth.Code', blank=True)),
                ('merged_with', models.ForeignKey(related_name='merged_set', blank=True,
                                                  to=settings.AUTH_USER_MODEL, null=True,
                                                  on_delete=models.CASCADE)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=5)),
                ('slug', models.SlugField()),
                ('identifier', models.CharField(unique=True, max_length=64)),
                ('title', models.TextField()),
                ('version', models.CharField(default=b'0', max_length=255)),
                ('verification_function_type', models.IntegerField(default=0, choices=[(0, b'internal'), (1, b'javascript')])),
                ('verification_function', models.TextField(default=b'', blank=True)),
                ('license', models.TextField(default=b'Creative commons CC-By')),
                ('language', models.CharField(max_length=7, choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')])),
                ('authors', models.TextField(default=b'Various')),
                ('accepted_answers', models.CommaSeparatedIntegerField(max_length=255, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('questions', models.ManyToManyField(to='bober_simple_competition.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relative_url', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to=b'resources')),
                ('resource_type', models.CharField(max_length=255)),
                ('data', models.BinaryField(null=True)),
                ('question', models.ForeignKey(to='bober_simple_competition.Question', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResourceCache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'caches')),
                ('format', models.CharField(max_length=16, choices=[(b'zip', b'ZIP'), (b'raw', b'raw data')])),
                ('resources', models.ManyToManyField(to='bober_simple_competition.Resource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questionset',
            name='resource_caches',
            field=models.ManyToManyField(to='bober_simple_competition.ResourceCache'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competitionquestionset',
            name='questionset',
            field=models.ForeignKey(to='bober_simple_competition.QuestionSet', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='questionsets',
            field=models.ManyToManyField(to='bober_simple_competition.QuestionSet', through='bober_simple_competition.CompetitionQuestionSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='competitionquestionset',
            field=models.ForeignKey(to='bober_simple_competition.CompetitionQuestionSet', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='invalidated_by',
            field=models.ForeignKey(related_name=b'invalidated_set', blank=True, to='bober_simple_competition.Profile',
                                    null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(to='bober_simple_competition.Profile', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='attempt',
            field=models.ForeignKey(to='bober_simple_competition.Attempt', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
