__author__ = 'Grega'

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from application.models import *

# default model for django's User: https://docs.djangoproject.com/en/dev/ref/contrib/auth/
class UserProfile(models.Model):

    # Linking UserProfile with default django's User table
    user = models.OneToOneField(User)

    # User profile parameters
    interface_lang_code = models.CharField(max_length=10, default="en")

    def selected_language(self):
        return 'en'

    def create_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = UserProfile.objects.get_or_create(user=instance)

    post_save.connect(create_profile, sender=User)


    # For syncdb to work
    class Meta:
        app_label = 'application'
