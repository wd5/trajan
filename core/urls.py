from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:

from core.api import LocationResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(LocationResource())


urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^photos/$', 'core.views.photos', name="photos_home"),
    url(r'^locations/$', 'core.views.locations', name="locations"),
    url(r'^locations/api/', include(v1_api.urls)),
    url(r'^locations/(?P<location_id>\d+)/$', 'core.views.location', name="location"),
    url(r'^(?P<page_slug>[-\w]+)/$', 'core.views.render_page'),
)