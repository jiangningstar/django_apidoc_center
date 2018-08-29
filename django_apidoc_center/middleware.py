# -*- coding:UTF-8 -*-


# TODO 先偷个懒
class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
