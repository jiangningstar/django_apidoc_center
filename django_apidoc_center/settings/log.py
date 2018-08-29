# -*- coding:UTF-8 -*-
import os

_ = os.environ.get('DJANGO_SETTINGS_MODULE', 'django_apidoc_center.settings.local')

if 'local' in _:
    from ..logconfig.local_log import LOGGING
if 'production' in _:
    from ..logconfig.production_log import LOGGING
if 'test' in _:
    from ..logconfig.test_log import LOGGING


def get_logging(log_root, log_level):
    log_conf = LOGGING
    for k in log_conf.get('handlers').keys():
        if 'filename' in log_conf['handlers'][k].keys():
            log_conf['handlers'][k]['filename'] = log_conf['handlers'][k]['filename'] % {'LOG_ROOT': log_root}
        if 'level' in log_conf['handlers'][k].keys():
            log_conf['handlers'][k]['level'] = log_level.get(k, log_conf['handlers'][k]['level'])
    return log_conf
