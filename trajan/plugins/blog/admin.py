from django.contrib import admin
# Import your models here.
from trajan.plugins.blog.models import *
from locations.models import Location
from django import forms
from django.conf import settings

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'category', 'location', 'published')
    save_on_top = True
    search_fields = ('title', 'category', 'location')
    actions = ['publish']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def publish(self, request, queryset):
        rows = queryset.update(published=True)
        if rows == 1:
            message_bit = "1 blog post was"
        else:
            message_bit = "%s blog posts were" % rows
        self.message_user(request, "%s successfully published." % message_bit)
        

            

        
admin.site.register(Post, PostAdmin)
admin.site.register(Status)

admin.site.register(Category)