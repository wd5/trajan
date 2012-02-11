from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from brew.models import *



class BeerResource(ModelResource):
    class Meta:
        queryset = Beer.objects.published()
        resource = 'post'
        allowed_methods = ['get']
        include_absolute_url = True
        always_return_data = True
        

