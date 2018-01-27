from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^check_register/$', views.check_register),
    url(r'^user/register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^check_login/$', views.check_login),
]
