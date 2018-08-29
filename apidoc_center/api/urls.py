# -*- coding:UTF-8 -*-

from views import ProjectsViewSet, ServicesViewSet
from rest_framework.routers import DefaultRouter
# from django.conf.urls import url
# from ..views import index

router = DefaultRouter()
router.register(r'projects', ProjectsViewSet, base_name='projects')
router.register(r'services', ServicesViewSet, base_name='services')

# urlpatterns = [
#     url(r'^home/$', index),
# ]

urlpatterns = router.urls

