# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

import os
import ast
from libs.gitlab_api import gl
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.conf import settings

from apidoc_center.models import Services

from libs.write_content import write_file


# TODO 这里不应该用信号操作, 应该放在对应的业务当中
@receiver(pre_save, sender=Services, dispatch_uid="Services_post_save")
def pull_build_files(sender, **kwargs):
    """
    生成项目文件夹和拉取服务文件夹以及文件

    :param sender:
    :param kwargs:
    :return:
    """

    instance = kwargs.get('instance')
    project_path = '/'.join([settings.GIT_PULL_FILE_PATH, instance.project.name, instance.name])
    if not os.path.exists(project_path):
        os.makedirs(project_path)

    project = gl.projects.get('%s/%s' % (instance.group, instance.name))
    file_path_list = ast.literal_eval(instance.file_path_list)
    for path in file_path_list:
        f = project.files.get(file_path=path, ref=instance.branch)
        if '.' in path:
            path = path.split('/')
            file_name = path.pop()
            file_path = '/'.join([project_path, '/'.join(path)])
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            write_file('/'.join([file_path, file_name]), f.decode())
