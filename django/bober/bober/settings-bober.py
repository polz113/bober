"""
Django settings for bober project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pb&ae^s3%52i5=$y#seb4vvsd6=$tegss%v5nyx#v(@jt%06t('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL="/"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bober_competition',
    'bober_paper_submissions',
    'code_based_auth',
    'bober_simple_competition',
    'bober_si',
    'bober_tasks',
    'social.apps.django_app.default',
    'taggit',
    'django_tables2',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    #'PIL',
    # 'autocomplete_light'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# config for Django 1.10 and later
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.core.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# config for older versions of Django

#TEMPLATE_DEBUG = True

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.static',
#    'django.core.context_processors.request',
#    'django.contrib.auth.context_processors.auth',
#    'django.contrib.messages.context_processors.messages',
#)

ROOT_URLCONF = 'bober.urls'

WSGI_APPLICATION = 'bober.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bober',
        'USER': 'bober',
        'PASSWORD': 'YOURPASSWORD',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'en-us'

TINYMCE_DEFAULT_CONFIG = {
  #'plugins': "table,spellchecker,paste,searchreplace",
  #'theme': "advanced",
  'file_browser_callback': 'mce_filebrowser',
  #'paste_as_text': True,
}

LANGUAGES = (
#    ('sl', _('Slovenian')),
#    ('sr_Latn', _('Serbian')),
#    ('hr', _('Croatian')),
#    ('tr', _('Turkish')),
    ('en', _('English')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/your/static/dir/path'
#filebrowser media settings
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/image/'
