# -*- coding: utf-8 -*-

import os
import dj_database_url
import raven

from django.conf import settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    '13e55w#)-&-#fuo4-m%bwp3x7=x%_$u8g80r&sg5_*d*c21hu+'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = os.getenv('ALLOWED_DOMAIN', 'localhost').split(',')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',

    'rest_framework',

    'octofiles.core',
    'octofiles.authentication',
)

if settings.DEBUG:
    INSTALLED_APPS += (
        'test_without_migrations',
    )

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'octofiles.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'octofiles.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Alem disso, usando o dj-database-url que configura o banco a partir
# da variavel de ambiente DATABASE_URL, e caso não encontre uma
# utiliza um valor padrão.

# https://pypi.python.org/pypi/dj-database-url
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://procult:123456@localhost/procult'
    )
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ALLOWED_FILES = [
    'application/pdf',
    'application/msword',
    'application/excel',
    'application/x-excel',
    'application/vnd.ms-excel',
    'application/x-msexcel',
    'application/powerpoint',
    'application/mspowerpoint',
    'application/x-mspowerpoint',
    'application/vnd.ms-powerpoint',
    'application/vnd.oasis.opendocument.text',
    'application/vnd.oasis.opendocument.presentation',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.sun.xml.writer',
    'application/vnd.sun.xml.writer.global',
    'application/vnd.sun.xml.impress',
    'application/vnd.sun.xml.draw',
    'application/vnd.sun.xml.calc',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.openxmlformats-officedocument.presentationml.slide',
    'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'application/x-7z-compressed',
    'application/zip',
    'application/x-rar-compressed',
    'image/png',
    'image/gif',
    'image/jpg',
    'image/jpeg',
    'image/pjpeg',
    'image/tiff',
    'image/x-tiff',
    'image/bmp',
    'image/x-windows-bmp',
    'audio/ogg',
    'audio/mpeg',
    'audio/mpeg3',
    'audio/mp3',
    'audio/mp4'
    'audio/x-mpeg-3',
    'audio/voc',
    'audio/wav',
    'audio/x-wav',
    'audio/aiff',
    'audio/x-aiff',
    'audio/midi',
    'audio/x-mid',
    'audio/x-midi',
    'audio/webm',
    'application/mp4',
    'application/x-troff-msvideo',
    'application/vnd.rn-realmedia',
    'application/ogg'
    'video/mp4',
    'video/mpeg',
    'video/ogg',
    'video/x-mpeg',
    'video/avi',
    'video/msvideo',
    'video/x-msvideo',
    'video/x-dv',
    'video/quicktime'
    'video/webm',
    'video/H261',
    'video/H263',
    'video/H263-1998',
    'video/H263-2000',
    'video/H264',
    'video/H264-RCDO',
    'video/H264-SVC '
]

# Django Rest Framework
REST_FRAMEWORK = {
    'DATE_FORMAT': "%d/%m/%Y",
    'DATE_INPUT_FORMATS': ["%d/%m/%Y", "%d/%m/%y"],
    'PAGE_SIZE': 100
}

# Local configuration
if settings.DEBUG:
    INSTALLED_APPS += (
        'corsheaders',
    )

    MIDDLEWARE_CLASSES = (
        'corsheaders.middleware.CorsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    CORS_ORIGIN_ALLOW_ALL = os.getenv('DEBUG', False)

    # Define CORS to allow client in development mode
    CORS_ORIGIN_WHITELIST = (
        'localhost:5000',
        'octofiles.local:5000',
        '0.0.0.0:5000',
    )
RAVEN_CONFIG = {
        'dsn': os.getenv('RAVEN_DSN_URL'),
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(BASE_DIR),
}
