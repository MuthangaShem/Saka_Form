"""
Django settings for sakaform project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

LOGIN_URL = ('accounts/login')
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'accounts/login'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%4l)p3$wm4qikr#&^64uiw487x&0drlz*+exd5x7v!excvxxgi'

# github auth
SOCIAL_AUTH_GITHUB_KEY = 'a7044dfaf7bc33816cba'
SOCIAL_AUTH_GITHUB_SECRET = '9805efb4bae009b15354e29fa458c68404b36a5d'

# twitter auth
SOCIAL_AUTH_TWITTER_KEY = '9TD12xahCWCDdyLzpmw61GSM9'
SOCIAL_AUTH_TWITTER_SECRET = 'QyKXLkkxvAAylfguI6RtPsmi2d5Q1vniPgqR0ZxMVMbdsRxuEk'

# social auth
SOCIAL_AUTH_FACEBOOK_KEY = '385298425305419'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd431451f2f6575be03d1d32038deb95b'

# social google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '486763413473-2gigi6rn844a1dimnrj31mocdquouefj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xBnhSUy67A73FAGvDNqbd8wH'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'app.apps.AppConfig',
    'social_django',
    'bootstrap4',
    'django_extensions',
    'bootstrap_datepicker_plus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'sakaform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'sakaform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'form',
#         'USER': 'mwangi',
#         'PASSWORD': 'T11111'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.db'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.twitter.TwitterOAuth',  # for Twitter authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication

    'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_TZ = True


# authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.twitter.TwitterOAuth',  # for Twitter authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId', # for Google authentication
    'social_core.backends.google.GoogleOAuth2', # for Google authentication

    'django.contrib.auth.backends.ModelBackend',
)


# github auth 
SOCIAL_AUTH_GITHUB_KEY = 'a7044dfaf7bc33816cba'
SOCIAL_AUTH_GITHUB_SECRET = '9805efb4bae009b15354e29fa458c68404b36a5d'

# twitter auth
SOCIAL_AUTH_TWITTER_KEY = '9TD12xahCWCDdyLzpmw61GSM9'
SOCIAL_AUTH_TWITTER_SECRET = 'QyKXLkkxvAAylfguI6RtPsmi2d5Q1vniPgqR0ZxMVMbdsRxuEk'

# social auth
SOCIAL_AUTH_FACEBOOK_KEY = '385298425305419' 
SOCIAL_AUTH_FACEBOOK_SECRET = 'd431451f2f6575be03d1d32038deb95b' 

# social google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='486763413473-2gigi6rn844a1dimnrj31mocdquouefj.apps.googleusercontent.com'  
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xBnhSUy67A73FAGvDNqbd8wH'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
<<<<<<< HEAD

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'accounts/login'



BOOTSTRAP4 = {
    'include_jquery': True,
}
=======
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
>>>>>>> 80c804fb7ff2f201d7acb9a3dec1230c0ce7cf85
