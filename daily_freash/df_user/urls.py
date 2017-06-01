from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^registerpost1/$', views.register_post1),
    url(r'^checkname/$', views.checkname),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
]
