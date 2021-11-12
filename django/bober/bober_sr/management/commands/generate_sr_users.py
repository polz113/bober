#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User

class Command(BaseCommand):
    # @transaction.atomic

    def make_manifest(dirname):
        pass
    
    def add_arguments(self, parser):
        parser.add_argument('n_of_users', type=int)
        
    def handle(self, n_of_users, **options):
        User.objects.filter(first_name='Dabar', 
                last_name__startswith='Glodavac').delete()
        username_format='dabar{{:0{}}}'.format(len(str(n_of_users)))
        email_format='{}@bober-rs.acm.si'.format(username_format)
        for i in range(1, n_of_users+1):
            u = User(first_name='Dabar', last_name='Glodavac {}.'.format(i), 
                    email=email_format.format(i), 
                    username=username_format.format(i))
            password = "".join([random.choice("qwertzupasdfghjkyxcvbnm23456789*+") for x in range(9)])
            u.set_password(password)
            sys.stdout.buffer.write("{},{},{},{},{}\n".format(u.first_name, u.last_name, u.email, u.username, password).encode("utf-8"))
            u.save()

