from django.db import models
from hadrian.utils.slugs import unique_slugify
from django.db.models.query import QuerySet
from brew.choices import *
from django.template.defaultfilters import truncatewords_html
from locations.models import Location

class BeerMixin(object):

    def published(self):
        return self.filter(published=True)
        
    def featured(self):
        return self.filter(featured=True)

class BeerQuerySet(QuerySet, BeerMixin):
    pass

class BeerManager(models.Manager, BeerMixin):
    def get_query_set(self):
        return BeerQuerySet(self.model, using=self._db)



class Beer(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    description = models.TextField()
    short_description = models.TextField(blank=True, editable=False)
    abv = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    original_gravity = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    final_gravity = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    ibu = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='brew/images/', blank=True)
    location = models.ForeignKey(Location)
    
    published = models.BooleanField()
    featured = models.BooleanField()
    
    objects = BeerManager()
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('brew.views.view_beer', (), {'beer_slug': self.slug})
    
    def save(self):
        unique_slugify(self, self.name)
        self.short_description = truncatewords_html(self.description, 40)
        super(Beer, self).save()