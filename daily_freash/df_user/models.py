#coding=utf-8

from django.db import models

# Create your models here.

# 用户名：18210569700
# 密码
# 联系方式：18210569700
#邮箱
# 联系地址：北京市昌平区
# 收获地址
# 邮编

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uaddr = models.CharField(max_length=100)
    uphone = models.CharField(max_length=20)
    uemail = models.CharField(max_length=20)
    ushou = models.CharField(max_length=100)
    uyoubian = models.CharField(max_length=20)


