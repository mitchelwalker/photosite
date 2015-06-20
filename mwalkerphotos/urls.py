from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'mwalkerphotos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.STATIC_ROOT,
        }),
    url(r"^albums/$", "homepage.views.albums"),    
    url(r"^albums/(?P<title>\w+)$", "homepage.views.album_view"),
   
    
)
