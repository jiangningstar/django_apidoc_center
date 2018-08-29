# -*- coding: utf-8 -*-

from .base import *

# DEFAULT_CHARSET = "UTF-8"

GUARDIAN_MONKEY_PATCH = False

DOMAIN_SMEDIA = '127.0.0.1:8000'

MEDIA_ROOT = '/data/www/htdocs/smedia/'
MEDIA_URL = '/smedia/'

LOG_ROOT = "/data/logs/linkedsee/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_apidoc_center',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
    }
}

LOG_LEVEL = {'root': 'DEBUG', }

from .log import *

LOGGING = get_logging(LOG_ROOT, LOG_LEVEL)
