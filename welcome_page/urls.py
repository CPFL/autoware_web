from django.conf.urls import url

from . import views

app_name = 'autoware_web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='mypage'),
    url(r'^$', views.index, name='login'),
    url(r'^$', views.index, name='logout'),
    url(r'^docker_x86/$', views.docker_x86_install, name='docker_x86'),
    url(r'^docker_px2/$', views.docker_px2_install, name='docker_px2'),
    url(r'^development/$', views.development, name='development'),
    url(r'^development2/$', views.development2, name='development2'),
]
