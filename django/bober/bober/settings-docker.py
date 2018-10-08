"""
Django settings for bober project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pb&ae^s3%52i5=$y#seb4vvsd6=$tegss%v5nyx#v(@jt%06t('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL="/"
# Application definition

INSTALLED_APPS = (
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bober_paper_submissions',
    'code_based_auth',
    'bober_simple_competition',
    'bober_si',
    'bober_tasks',
    'social_django',
    'taggit',
    'django_tables2',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'popup_modelviews',
    'crispy_forms',
    'impersonate',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Disable LocaleMiddleware to disable
    # language detection and use default language
    # set by LANGUAGE_CODE    
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'bober_simple_competition.middleware.ProfileMiddleware',
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
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
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

import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',   
        'NAME': 'bober',
        'USER': 'bober',
        'PASSWORD': 'database_password',
        'HOST': 'db',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'bober',
#        'USER': 'bober',
#        'PASSWORD': 'YOURPASSWORD',
#        'HOST': 'localhost',
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'sl'

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


AUTHENTICATION_BACKENDS = (
#    'social.backends.amazon.AmazonOAuth2',
#    'social.backends.angel.AngelOAuth2',
#    'social.backends.aol.AOLOpenId',
#    'social.backends.appsfuel.AppsfuelOAuth2',
#    'social.backends.beats.BeatsOAuth2',
#    'social.backends.behance.BehanceOAuth2',
#    'social.backends.belgiumeid.BelgiumEIDOpenId',
#    'social.backends.bitbucket.BitbucketOAuth',
#    'social.backends.box.BoxOAuth2',
#    'social.backends.clef.ClefOAuth2',
#    'social.backends.coinbase.CoinbaseOAuth2',
#    'social.backends.coursera.CourseraOAuth2',
#    'social.backends.dailymotion.DailymotionOAuth2',
#    'social.backends.disqus.DisqusOAuth2',
#    'social.backends.douban.DoubanOAuth2',
#    'social.backends.dropbox.DropboxOAuth',
    'social_core.backends.dropbox.DropboxOAuth2',
#    'social.backends.eveonline.EVEOnlineOAuth2',
#    'social.backends.evernote.EvernoteSandboxOAuth',
#    'social.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
#    'social.backends.fedora.FedoraOpenId',
#    'social.backends.fitbit.FitbitOAuth',
#    'social.backends.flickr.FlickrOAuth',
#    'social.backends.foursquare.FoursquareOAuth2',
    'social_core.backends.github.GithubOAuth2',
    # 'social.backends.google.GoogleOAuth',
    'social_core.backends.google.GoogleOAuth2',
#    'social.backends.google.GoogleOpenId',
#    'social.backends.google.GooglePlusAuth',
#    'social.backends.google.GoogleOpenIdConnect',
#    'social.backends.instagram.InstagramOAuth2',
#    'social.backends.jawbone.JawboneOAuth2',
#    'social.backends.kakao.KakaoOAuth2',
#    'social.backends.linkedin.LinkedinOAuth',
#    'social.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.live.LiveOAuth2',
    'social_core.backends.livejournal.LiveJournalOpenId',
#    'social.backends.mailru.MailruOAuth2',
#    'social.backends.mendeley.MendeleyOAuth',
#    'social.backends.mendeley.MendeleyOAuth2',
#    'social.backends.mineid.MineIDOAuth2',
#    'social.backends.mixcloud.MixcloudOAuth2',
#    'social.backends.nationbuilder.NationBuilderOAuth2',
#    'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.openstreetmap.OpenStreetMapOAuth',
#    'social.backends.persona.PersonaAuth',
#    'social.backends.podio.PodioOAuth2',
#    'social.backends.rdio.RdioOAuth1',
#    'social.backends.rdio.RdioOAuth2',
#    'social.backends.readability.ReadabilityOAuth',
    'social_core.backends.reddit.RedditOAuth2',
#    'social.backends.runkeeper.RunKeeperOAuth2',
#    'social.backends.skyrock.SkyrockOAuth',
#    'social.backends.soundcloud.SoundcloudOAuth2',
#    'social.backends.spotify.SpotifyOAuth2',
#    'social.backends.stackoverflow.StackoverflowOAuth2',
#    'social.backends.steam.SteamOpenId',
#    'social.backends.stocktwits.StocktwitsOAuth2',
#    'social.backends.stripe.StripeOAuth2',
#    'social.backends.suse.OpenSUSEOpenId',
#    'social.backends.thisismyjam.ThisIsMyJamOAuth1',
#    'social.backends.trello.TrelloOAuth',
#    'social.backends.tripit.TripItOAuth',
#    'social.backends.tumblr.TumblrOAuth',
#    'social.backends.twilio.TwilioAuth',
#    'social.backends.twitter.TwitterOAuth',
#    'social.backends.vk.VKOAuth2',
#    'social.backends.weibo.WeiboOAuth2',
#    'social.backends.wunderlist.WunderlistOAuth2',
#    'social.backends.xing.XingOAuth',
#    'social.backends.yahoo.YahooOAuth',
#    'social.backends.yahoo.YahooOpenId',
#    'social.backends.yammer.YammerOAuth2',
#    'social.backends.yandex.YandexOAuth2',
#    'social.backends.vimeo.VimeoOAuth1',
#    'social.backends.lastfm.LastFmAuth',
#    'social.backends.moves.MovesOAuth2',
#    'social.backends.vend.VendOAuth2',
#    'social.backends.email.EmailAuth',
#    'social.backends.username.UsernameAuth',
#    'djangosaml2.backends.Saml2Backend',
    'django.contrib.auth.backends.ModelBackend',
#    'bober_auth.auth.BoberCompetitionAuthBackend',
)


