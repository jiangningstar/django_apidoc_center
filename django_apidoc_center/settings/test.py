# -*- coding: utf-8 -*-

from .base import *

# DEFAULT_CHARSET = "UTF-8"

GUARDIAN_MONKEY_PATCH = False

DOMAIN_SMEDIA = '127.0.0.1:8000'

MEDIA_ROOT = '/data/www/htdocs/smedia/'
MEDIA_URL = '/smedia/'

LOG_ROOT = "/data/logs/linkedsee/"

# test databases
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

LOG_LEVEL = {'root': 'DEBUG', }

from .log import *

LOGGING = get_logging(LOG_ROOT, LOG_LEVEL)
