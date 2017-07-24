
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls), #when i write the admin in the url it will open the admin page
    url(r'^posts/', include('posts.urls', namespace='posts')) # to access the urls in the post      ^this is to define where the url begin	/namespace we use it if we have same url name for anothe url app
]
