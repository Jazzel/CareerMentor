"""
Django settings for the_career_mentor project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# import mysql.connector as cn

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dg71n=11pahp^(0*as3f^j&j^=hrmp&=kp26629(ez%g@p2p$z'

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
    'rest_framework',
    'knox',
    ##
    'corsheaders',
    ##
    'App1',
]

##
CORS_ORIGIN_ALLOW_ALL = True
##
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ##
    'corsheaders.middleware.CorsMiddleware',
    ##
]

ROOT_URLCONF = 'the_career_mentor.urls'
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
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

WSGI_APPLICATION = 'the_career_mentor.wsgi.application'


# obj = cn.connect (
#     host  = 'localhost',
#     user = 'root',
#     password = 'starbareeha123',
#     database= 'db_tcm'
# )

# cr = obj.cursor()

# sql="insert into user_login_info (username,password,email) values ('Sbareeha','star123','sybareeha')"
# cr.execute(sql)
# obj.commit()
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': 
    {
      'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        ###########################
        #Up till now Want to use mysql but facing installment 
        #issues in mysqlclient due to missing .h files
        ###########################
    #     'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'db_tcm',
    #     'USER': 'root',
    #     'PASSWORD': 'starbareeha123',
    #     'HOST':'localhost',
    #     'PORT':'3306',
    }
    #}
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ]
}

#########################################

# These are the default values if none are set 
from datetime import timedelta
from rest_framework.settings import api_settings
REST_KNOX = {
    'SECURE_HASH_ALGORITHM':'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64, # By default, it is set to 64 characters (this shouldn't need changing).
    'TOKEN_TTL': timedelta(minutes=45), # The default is 10 hours i.e., timedelta(hours=10)).
    'USER_SERIALIZER': 'knox.serializers.UserSerializer',
    'TOKEN_LIMIT_PER_USER': None, # Edit: By default it was 0..., this option is disabled and set to None -- thus no limit.
    'AUTO_REFRESH': False, # This defines if the token expiry time is extended by TOKEN_TTL each time the token is used.
    'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
}

##Today##
# AUTH_USER_MODEL = 'App1.CustomUser'
