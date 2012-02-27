from trajan.core.models import *
from django.contrib import admin


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)