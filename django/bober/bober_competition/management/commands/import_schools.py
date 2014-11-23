#!/usr/bin/python
# -*- coding: utf8 -*-


from django.core.management.base import BaseCommand
from django.db import transaction
from bober_competition.models import *
import csv

class Command(BaseCommand):
    # @transaction.atomic
    def handle(self, *args, **options):
        competition = Competition.objects.get(name = args[0])
        with open(args[1], 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title_row = spamreader.next()
            print title_row
            for row in spamreader:
                name, school_category_id, level_of_education, post, postal_code, municipality_name, region_name, country = row
                country, created = Country.objects.get_or_create(country=country)
                municipality, created = Municipality.objects.get_or_create(country=country, name=municipality_name)
                region, created = Region.objects.get_or_create(country=country, name=region_name)
                try:
                    s = School.objects.get(name = name)
                    name = s.name + u", " + municipality_name.decode('utf-8')
                except Exception, e:
                    print e
                s = School(
                    name = name,
                    school_category_id = int(school_category_id),
                    level_of_education = level_of_education,
                    post = post,
                    postal_code = postal_code,
                    municipality = municipality,
                    region = region,
                    country = country
                )
                s.save()
                print ', '.join(row)
