from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^blog/', include('blog.urls')),
    #url(r'beers/', include('brew.urls')),
    #url(r'bookmarks/', include('bookmarks.urls')),
    #url(r'trips/', include('traveler.urls')),    
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r'^', include('trajan.core.urls')),
)