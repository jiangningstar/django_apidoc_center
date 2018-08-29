# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from .serializers import ProjectsSerializer, ServicesSerializer, ProjectsRetrieveSerializer
from ..models import Projects, Services


class ProjectsViewSet(viewsets.GenericViewSet):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        queryset = Projects.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        """
        获取所有项目

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.get_queryset()
        serializer = ProjectsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        获取单个项目以及关联服务

        :param request:
        :param pk:
        :return:
        """
        queryset = self.get_queryset()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectsRetrieveSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        """
        创建项目

        :param request:
        :return:
        """
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        更新项目信息

        :param request:
        :param pk:
        :return:
        """
        queryset = self.get_queryset()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        删除项目, 关联服务会一起删除

        :param request:
        :return:
        """
        queryset = self.get_queryset()
        project = get_object_or_404(queryset, pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServicesViewSet(viewsets.GenericViewSet):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        queryset = Services.objects.all()
        return queryset

    def create(self, request):
        """
        创建项目关联的服务

        :param request:
        :return:
        """
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        更新单个服务的信息

        :param request:
        :param pk:
        :return:
        """
        queryset = self.get_queryset()
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServicesSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        删除一个服务

        :param request:
        :param pk:
        :return:
        """
        queryset = self.get_queryset()
        service = get_object_or_404(queryset, pk=pk)
        service.delete()
        return Response('delete')
