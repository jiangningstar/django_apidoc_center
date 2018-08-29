# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ApidocCenterConfig(AppConfig):
    name = 'apidoc_center'

    def ready(self):
        import apidoc_center.signals.handlers
