from django.conf.urls.defaults import patterns, include, url
# Import your views and feeds from your app.
from brew.views import *
from brew.api import BeerResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(BeerResource())

urlpatterns = patterns('',
    
    url(r'^$', beers, name="view_beer"),
    url(r'^api/', include(v1_api.urls)),
    url(r'^(?P<beer_slug>[-\w]+)/$', view_beer, name="view_beer"),
    
)
