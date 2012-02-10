from tastypie.resources import ModelResource
from tastypie import fields
from locations.models import *



class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource = 'location'
        allowed_methods = ['get']
