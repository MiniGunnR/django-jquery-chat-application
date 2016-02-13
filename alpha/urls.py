from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Login, name='login'),

    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^home/$', views.Home, name='home'),

    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),

    url(r'^test/$', views.test, name='test'),
]