from django.conf.urls import url

from . import views

app_name = 'autoware_web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.index, name='mypage'),
    # url(r'^$', views.index, name='login'),
    # url(r'^$', views.index, name='logout'),
    url(r'^docker_x86/$', views.docker_x86_install, name='docker_x86'),
    url(r'^docker_px2/$', views.docker_px2_install, name='docker_px2'),
    #url(r'^development/$', views.development, name='development'),
    url(r'^join/$', views.join, name='join'),
    # url(r'^development/$', views.development, name='development'),
    # url(r'^development2/$', views.development2, name='development2'),
    url(r'^sample/sample_moriyama_data.tar.gz/$', views.sample_data1, name='sample_moriyama_data.tar.gz'),
    url(r'^sample/my_launch.sh/$', views.sample_data2, name='my_launch.sh'),
    url(r'^sample/sample_moriyama_150324.tar.gz/$', views.sample_data3, name='sample_moriyama_150324.tar.gz'),
    url(r'^docker/drive_px2/autoware_container_image_latest.tar$', views.docker_image_px2, name='docker_image_px2'),
]
