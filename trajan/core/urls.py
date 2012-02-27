from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',

    url(r'^(?P<page_slug>[-\w]+)/$', 'trajan.core.views.render_page'),
)