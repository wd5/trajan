from django.db import models
from django.contrib.auth.models import User
from hadrian.utils.slugs import unique_slugify
# Import Tagging
from hadrian.dist.tagging.fields import TagField
from hadrian.dist.tagging.models import Tag
from xml.etree import ElementTree
# For use with model managers.
from django.db.models.query import QuerySet
from django.template.defaultfilters import truncatewords_html
from locations.models import Location
import twitter
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
    tags = TagField()
    category = models.ForeignKey(Category, blank=True, null=True)
    fotochest_api_call = models.CharField(max_length=350, blank=True, null=True, default='')
    published_date = models.DateField(auto_now=True, auto_now_add=True)
    location = models.ForeignKey(Location)
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    
    
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
    
class Status(models.Model):
    tweet = models.CharField(max_length=250)
    twitter_id = models.BigIntegerField()
    created_at = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    
    def __unicode__(self):
        return self.tweet
    
    class Meta:
        ordering = ['-twitter_id']
    

def status_sync():
    from django.contrib.localflavor.us import us_states
    twitter_api = twitter.Api()
    try:
        statuses = twitter_api.GetUserTimeline("derekstegelman")
    except:
        pass
        return HttpResponse("ok", mimetype="text/plain")
    for tweets in statuses:
        try:
            get_status = Status.objects.get(twitter_id=tweets.id)
        except Status.DoesNotExist:
            new_tweet = Status(tweet=tweets.text)
            new_tweet.twitter_id = tweets.id
            new_tweet.created_at = tweets.created_at
            try:
                if tweets.place:
                    if tweets.place["place_type"] == "city":
                        loc = Location.objects.get(city=tweets.place["name"])
                    else:
                        loc = Location.objects.get(pk=1)
                else:
                    loc = Location.objects.get(pk=1)
            except Location.DoesNotExist:
                loc = Location(city=tweets.place["name"])
                import string
                loc.state = string.split(tweets.place["full_name"], ", ")[1]
                loc.country = tweets.place["country"]
                loc.save()

            new_tweet.location = loc
            new_tweet.save()
    
