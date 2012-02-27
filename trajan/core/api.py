from tastypie.resources import ModelResource
from tastypie import fields
from trajan.core.models import *


class PageResource(ModelResource):
    class Meta:
        queryset = Page.objects.all()
        resource = 'page'
        allowed_methods = ['get']


