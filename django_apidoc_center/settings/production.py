# -*- coding: utf-8 -*-

from .base import *

# DEFAULT_CHARSET = "UTF-8"

DEBUG = False

GUARDIAN_MONKEY_PATCH = False

DOMAIN_SMEDIA = '127.0.0.1:8000'

MEDIA_ROOT = '/data/www/htdocs/smedia/'
MEDIA_URL = '/smedia/'

LOG_ROOT = "/data/logs/linkedsee/"

LOG_LEVEL = {'root': 'DEBUG', }

from .log import *

LOGGING = get_logging(LOG_ROOT, LOG_LEVEL)
