from django.contrib import admin
from traveler.models import *

class TripAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ('title', 'locations')
    list_display = ('title', 'date_created', 'published', 'view')
    
    def view(self, obj):
        return "<a href='%s' target='_blank'>View</a>" % obj.get_absolute_url()
    view.allow_tags = True
    
    class Meta:
        model = Trip
        

admin.site.register(Trip, TripAdmin)
