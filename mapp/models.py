# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class PROJECT(models.Model):
    id = models.AutoField(primary_key=True)
    enum_type = (
        (0,""),
        (1,"理论"),
        (2,"实践"),
        (3,"消息"),
    )
    title = models.CharField(max_length=200)
    enum_state = (
        (0,""),
        (1,"编辑"),
        (2,"发布"),
        (3,"已完成"),
    )
    type = models.CharField(
        max_length=1,
        choices=enum_type,
        default = 0, 
    )
    state = models.CharField(
        max_length=1,
        choices=enum_state,
        default = 0 ,
    )
    student = models.CharField(max_length=200)
