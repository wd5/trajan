from django.conf.urls.defaults import patterns, include, url
from traveler.views import *
from traveler.api import TripResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(TripResource())

urlpatterns = patterns('',
    url(r'^$', trips, name="locations"),
    url(r'^trip/(?P<trip_slug>[-\w]+)/$', trip),
    url(r'^api/', include(v1_api.urls)),
)
