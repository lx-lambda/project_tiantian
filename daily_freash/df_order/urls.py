# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.order),
    url(r'commit/$', views.order_commit),
    url(r'pay(\d+)/$', views.pay),
]

