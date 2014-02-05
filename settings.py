"""
Django settings for clipper project.

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
SECRET_KEY = '7zvu(tvl5y_x&ue6o520k*bbsz(yf#x2=efcx3%x^ht@7#tfn1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'registration',
    'social_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'clipper.urls'

WSGI_APPLICATION = 'clipper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#To fix date data to login with SNS
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)


TEMPLATE_DIRS = (
    str(BASE_DIR + '/templates'),# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

LOGIN_URL          = '/'
#LOGIN_ERROR_URL    = '/login-error/'
LOGIN_REDIRECT_URL = "/home/"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window to confirm e-mail; used by the regisration app

################################################################
# Server email settings
################################################################

# See this easy article for configuring Postfix to send mail from Mac OSX
# http://www.developerfiles.com/how-to-send-smtp-mails-with-postfix-mac-os-x-10-8/

SERVER_EMAIL = "server@clipper.jp"
DEFAULT_FROM_EMAIL = 'no-reply@clipper.jp'

EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'admin@clipper.jp'
EMAIL_HOST_PASSWORD = 'pw'
EMAIL_PORT = 587

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

EMPLATE_CONTEXT_PROCESSORS = (
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

FACEBOOK_APP_ID='692933284060564'
FACEBOOK_API_SECRET='08495e8ce01c77d68cf981a0b32af4bf'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
TWITTER_CONSUMER_KEY         = 'mgcg6I1nQ9cHWbmXgf8qng'
TWITTER_CONSUMER_SECRET      = 'GqKd1eRRsRvaSR4kkEnD1PZpvig98w0kJs5Suyaqek'
GOOGLE_OAUTH2_CLIENT_ID = '720786611761-et4m0dle6acd0qlbulihhan7d2rvsmpj.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'wDmJweqGy0vsmXI-sBI3yzp8'

#Twitter doesn't provide email address, thus can't be unique in SNS login
#SOCIAL_AUTH_PIPELINE = (
 #   'social_auth.backends.pipeline.social.social_auth_user',
  #'social_auth.backends.pipeline.associate.associate_by_email', # To make email address unique
  #  'social_auth.backends.pipeline.user.get_username',
   # 'social_auth.backends.pipeline.custom_create_user',
    #'social_auth.backends.pipeline.social.associate_user',
    #'social_auth.backends.pipeline.social.load_extra_data',
    #'social_auth.backends.pipeline.user.update_user_details'
#)




