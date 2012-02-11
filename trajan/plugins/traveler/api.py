from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from traveler.models import *
from blog.api import LocationResource, PostResource

class TripResource(ModelResource):
    post = fields.ToManyField(PostResource, 'posts')
    location = fields.ToManyField(LocationResource, 'locations')
    class Meta:
        queryset = Trip.objects.all()
        resource = 'trip'
        allowed_methods = ['get']

