# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 21:44
from __future__ import unicode_literals

from django.db import migrations, models

def shorten_school_name(school_name):
    replacements = [(u"Osnovna šola", u"OŠ"), (u"Biotehniški izobraževalni center", u"BIC"),
                    (u"Šolski center", u"ŠC"), (u"Srednja šola", u"SŠ")]
    splits = {s.replace("*", " "): s.split("*") for s in
              (u"OŠ Sečovlje*Podružnična šola in vrtec Sveti Peter",
               u"ŠC Kranj,*SŠ za elektrotehniko in računalništvo",
               u"ŠC Novo mesto,*Srednja gradbena, lesarska in vzgojiteljska šola",
               u"ŠC Novo mesto,*Srednja elektro šola in tehniška gimnazija",
               u"OŠ Belokranjskega odreda Semič*Podružnična šola Štrekljevec",
               u"Elektrotehniško-računalniška strokovna*šola in gimnazija Ljubljana",
               u"ŠC Celje, SŠ za kemijo,*elektrotehniko in računalništvo",
               u"Zavod Antona Martina Slomška,*Škofijska gimnazija Antona Martina Slomška",
               u"ŠC Krško - Sevnica,*Srednja poklicna in strokovna šola Krško",
               u"Srednja vzgojiteljska šola*in gimnazija Ljubljana",
               u"Gimnazija in srednja šola*Rudolfa Maistra Kamnik",
               u"ŠC za pošto, ekonomijo in telekomunikacije*" \
                   u"Ljubljana, Srednja tehniška in strokovna šola",
               u"OŠ Antona Ingoliča Spodnja Polskava*Podružnica Zgornja Polskava",
               u"ŠC Slovenske Konjice - Zreče,*Gimnazija Slovenske Konjice",
               u"Gimnazija in ekonomska srednja šola*Trbovlje",
               u"Srednja gradbena, geodetska*in okoljevarstvena šola Ljubljana",
               u"OŠ Log - Dragomer,*Podružnična šola Bevke",
               u"Srednja tehniška in poklicna šola*Trbovlje",
               u"OŠ Prežihovega Voranca*Ravne na Koroškem",
               u"Šolski center Nova Gorica,*Gimnazija in zdravstvena šola",
               u"Osnovna šola Franca Rozmana - Staneta*Ljubljana",
               u"Srednja poklicna in tehniška šola*Murska Sobota",
               u"ŠC Nova Gorica,*Gimnazija in zdravstvena šola",
               u"Srednja tehniška šola*J. Vege v Gorici (Italija)",
               u"OŠ Franca Lešnika - Vuka*Slivnica pri Mariboru",)
             }
    if len(school_name) > 30:
        school_name = reduce(lambda x, r: x.replace(*r), replacements, school_name)
    if u"Podružnica" in school_name:
        school_name = school_name[:school_name.index(u"Podružnica") - 1]
    school_name = u"\n".join(splits.get(school_name, (school_name,)))
    if len(school_name) > 35 and school_name.find("\n") == -1:
        school_name.replace(", ", ",\n")
    return school_name


def school_display_names(apps, schema_editor):
    School = apps.get_model("bober_si", "School")
    for school in School.objects.all():
        school.display_name = shorten_school_name(school.name)
        school.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bober_si', '0004_auto_20160913_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='display_name',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(school_display_names, reverse_code=migrations.RunPython.noop),
    ]
