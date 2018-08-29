from django.db import models


# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)


class Services(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    file_path_list = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Projects, related_name='services')
