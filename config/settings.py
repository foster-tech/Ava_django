"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path,os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

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
    'ava',
    'bootstrap5',
    'rest_framework',
    'usuarios',
    'dynamic_models',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

TEMPLATES_PATH = os.path.join(BASE_DIR)

TEMPLATES_DIRS = (
    TEMPLATES_PATH,
)

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES_COMMON = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'PORT': '5432',
    }
}

DATABASES_PROD = {
    'default': {
        'NAME': 'fncrexox',
        'USER': 'fncrexox',
        'PASSWORD': '0uiQiWxL26POjrn62sPXVYYVL80vAVlY',
        'HOST': 'mahmud.db.elephantsql.com',
        **DATABASES_COMMON['default'],
    }
}


DATABASES_STAGE = {
    'default': {
        'NAME': os.environ.get('STAGE_DB_NAME', str(os.getenv('STAGE_NAME'))),
        'USER': os.environ.get('STAGE_DB_USER', str(os.getenv('STAGE_USER'))),
        'PASSWORD': os.environ.get('STAGE_DB_PASS', str(os.getenv('STAGE_PASSWORD'))),
        'HOST': 'staging-database-host',
        **DATABASES_COMMON['default'],
    }
}

DJANGO_ENV = 'production'

if DJANGO_ENV == 'production':
    DATABASES = DATABASES_PROD
elif DJANGO_ENV == 'staging':
    DATABASES = DATABASES_STAGE
else:
    DATABASES = DATABASES_COMMON



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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'config/static') 
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'usuarios.CustomUser'
