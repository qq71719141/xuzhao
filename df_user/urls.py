from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^check_register/$', views.check_register),
    url(r'^user/register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^check_login/$', views.check_login),
    url(r'^index/$', views.index),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^cart/$', views.cart),
    url(r'^detail/$', views.detail),
    url(r'^list/$', views.list),
    url(r'^place_order/$', views.place_order),
    url(r'^login_out/$', views.login_out),
    # url(r'^add_addr/$', views.add_addr),
]
