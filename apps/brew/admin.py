from django.contrib import admin
from brew.models import *
from django import forms


class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('http://static.derekandlindy.com/staging/iroam/javascript/ckeditor/ckeditor.js',)
        
        

        
admin.site.register(Beer, BeerAdmin)