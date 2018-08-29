# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator
from ..models import Projects, Services
import ast


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(
                queryset=Projects.objects.all(),
                fields=('name',)
            )
        ]


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"
        extra_kwargs = {'project': {'write_only': True}}

        validators = [
            UniqueTogetherValidator(
                queryset=Services.objects.all(),
                fields=('name',)
            )
        ]

    def to_representation(self, instance):
        ret = super(ServicesSerializer, self).to_representation(instance)
        ret['file_path_list'] = ast.literal_eval(ret['file_path_list'])
        return ret


class ProjectsRetrieveSerializer(ProjectsSerializer):
    services = ServicesSerializer(many=True, read_only=True)
