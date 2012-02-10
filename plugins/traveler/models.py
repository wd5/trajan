from django.db import models
from locations.models import Location
from hadrian.utils.slugs import unique_slugify
from blog.models import Post

class TripManager(models.Manager):
    def published(self):
        return Trip.objects.filter(published=True)

class Trip(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False, blank=True, null=True)
    trip_start_date = models.DateField()
    trip_end_date = models.DateField()
    date_created = models.DateField(auto_now=True, editable=False)
    description = models.TextField(null=True, blank=True)
    posts = models.ManyToManyField(Post, null=True, blank=True)
    locations = models.ManyToManyField(Location, null=True, blank=True)
    image = models.ImageField(upload_to="trip_images", blank=True, null=True)
    fotochest_api_call = models.CharField(max_length=350, blank=True, null=True, default='')
    published = models.BooleanField(default=False)
    
    objects = TripManager()
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Trip, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('traveler.views.trip', (), {'trip_slug': self.slug})
    