from django.conf.urls import url
import views


urlpatterns = [

    url(r'^register/$', views.register),
    url(r'^registerpost1/$', views.register_post1),
    url(r'^checkname/$', views.checkname),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order(\d?)/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^logout/$', views.logout),


]
