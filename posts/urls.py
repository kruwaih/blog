from django.conf.urls import url
from . import views #should import this line

urlpatterns = [
  
    url(r'^create/$', views.post_create, name = 'create'), #when i open 127.0.0.1:8000/create     $to definde where the url end
    url(r'^update/$', views.post_update, name = 'update'), #when i open 127.0.0.1:8000/update 
    url(r'^delete/$', views.post_delete, name = 'delete'),
    url(r'^list/$', views.post_list, name = 'list'),
    url(r'^detail/$', views.post_detail, name = 'detail'),
    
]
