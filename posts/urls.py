from django.conf.urls import url
from . import views #should import this line

urlpatterns = [
  
    # url(r'^create/$', views.create, name = 'create'), #when i open 127.0.0.1:8000/create     $to definde where the url end
    url(r'^update/(?P<slug>[-\w]+)/$', views.post_update, name = 'update'), #when i open 127.0.0.1:8000/update 
    url(r'^delete/(?P<slug>[-\w]+)/$', views.post_delete, name = 'delete'),
    url(r'^list/$', views.post_list, name = 'list'),
    url(r'^detail/(?P<slug>[-\w]+)/$', views.post_detail, name='detail'),
    url(r'^create/$', views.post_create, name = 'create'),
    url(r'^signup/$', views.usersignup, name = 'signup'),
    url(r'^login/$', views.userlogin, name = 'login'),
    url(r'^like_button/(?P<post_id>[\d]+)/$', views.like_button, name='like_button'),
    
]
