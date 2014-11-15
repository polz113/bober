import bober_competition.models
from django.conf import settings
from django.contrib.auth.models import User, check_password
import hashlib
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class BoberCompetitionAuthBackend(object):
    def authenticate(self, username=None, password=None):
        is_superuser = False
        #is_superuser = (settings.ADMIN_LOGIN == username)
        login_valid = False
        pwd_valid = False
        #print username, password
        if is_superuser:
            login_valid = True
        try:
            bober_user = bober_competition.models.Users.objects.get(username=username)
            #print "got bober user"
            pwd_valid = (bober_user.password == hashlib.sha512(password).hexdigest())
            #print bober_user.password, hashlib.sha512(password).hexdigest()
            first_name = bober_user.profile.first_name
            last_name = bober_user.profile.last_name
            login_valid = True
        except bober_competition.models.Users.DoesNotExist:
            login_valid = False
            first_name = username
            last_name = None
        print login_valid, pwd_valid
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. Note that we can set password
                # to anything, because it won't be checked; the password
                # from settings.py will.
                user = User(username=username, password='get from bober or settings')
                user.first_name = first_name
                user.last_name = last_name
                user.is_staff = is_superuser
                user.is_superuser = is_superuser
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
