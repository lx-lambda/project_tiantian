# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'detail(\d+)/$', views.detail),
    url(r'list(\d+)_(\d+)_(\d+)/$', views.list)
]

