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
    'django_coverage',
    'debug_toolbar',
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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clipper',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


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

LOGIN_REDIRECT_URL = "/home/"


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

### DJANGO-PAYPAL SETTINGS
PAYPAL_TEST = True
PAYPAL_WPP_USER = "???"
PAYPAL_WPP_PASSWORD = "???"
PAYPAL_WPP_SIGNATURE = "???"
PAYPAL_RECEIVER_EMAIL = "anuzis@gmail.com"

### DJANGO-REGISTRATION SETTINGS
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
