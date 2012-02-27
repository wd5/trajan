from django.db import models
from hadrian.utils.slugs import unique_slugify

class Category(models.Model):
    ''' Category Model '''
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, editable=False)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('view', (), {'slug': self.slug})
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Category, self).save(*args, **kwargs)
        
class Page(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Page, self).save(*args, **kwargs)
        
    def preview(self):
        return '<a href="%s?preview=true" target="_blank">Preview</a>' % self.get_absolute_url()
    preview.allow_tags = True
        
    @models.permalink
    def get_absolute_url(self):
        return ('trajan.core.views.render_page', (), {'page_slug': self.slug})