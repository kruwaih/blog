
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls), #when i write the admin in the url it will open the admin page
    url(r'^posts/', include('posts.urls', namespace='posts')), # to access the urls in the post      ^this is to define where the url begin	/namespace we use it if we have same url name for anothe url app
    url(r'^comments/', include('django_comments.urls')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^googleApp/', include('googleApp.urls', namespace='googleApp')),
    url(r'^accounts/', include('allauth.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)