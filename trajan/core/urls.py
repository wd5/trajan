from django.conf.urls.defaults import patterns, include, url
from trajan.core.api import PageResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(PageResource())

urlpatterns = patterns('',

    url(r'^(?P<page_slug>[-\w]+)/$', 'trajan.core.views.render_page'),
    url(r'^pages/api/', include(v1_api.urls)),
)