from django.db import models
from django.contrib.auth.models import User
from hadrian.utils.slugs import unique_slugify

from taggit.managers import TaggableManager
from xml.etree import ElementTree
# For use with model managers.
from django.db.models.query import QuerySet
from django.template.defaultfilters import truncatewords_html
from locations.models import Location

import string
from django.http import HttpResponse

'''
    Define model managers here.

'''

class PostMixin(object):
    def by_author(self, user):
        return self.filter(user=user)

    def published(self):
        return self.filter(published=True)
    
    def by_category(self, category_slug):
        return self.filter(category__slug=category_slug)

class PostQuerySet(QuerySet, PostMixin):
    pass

class PostManager(models.Manager, PostMixin):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.category', (), {'category_slug': self.slug})
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Category, self).save(*args, **kwargs)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    author = models.ForeignKey(User, editable=False)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, editable=False, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    published_date = models.DateField(auto_now=True, auto_now_add=True)
    location = models.ForeignKey(Location)
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    tags = TaggableManager()
    
    published = models.BooleanField()
    objects = PostManager()
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.post', (), {'post_slug': self.slug, 'year': self.published_date.year, 'month': self.published_date.month, 'day': self.published_date.day})
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        self.summary = truncatewords_html(self.content, 40)
        super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-id']
        
    
    '''
        Include your object (single instance) methods here.  Methods for multiple objects
        should be included in the object manager at the top of the module.
    
    '''
    

    
