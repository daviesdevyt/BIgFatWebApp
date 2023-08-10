from django.contrib import admin
from .models import News, CC, Fullz, Logs, Guides, Services, Dumps, Order, CCBase

# Register your models here.
admin.site.register(News)

@admin.register(CC)
class CCAdmin(admin.ModelAdmin):
    list_display = ('base', 'country', 'state', 'purchased', 'date_created')
    list_filter = ('base', 'country', 'state', 'purchased', 'date_created')
    search_fields = ('base', 'country', 'state')
    ordering = ('-date_created',)
    list_per_page = 25

@admin.register(Fullz)
class FullzAdmin(admin.ModelAdmin):
    list_display = ('category', 'country', 'purchased', 'date_created')
    list_filter = ('category', 'country', 'purchased', 'date_created')
    search_fields = ('base', 'country', 'state')
    ordering = ('-date_created',)

admin.site.register(Logs)
admin.site.register(Guides)
admin.site.register(Services)
admin.site.register(CCBase)

@admin.register(Dumps)
class DumpsAdmin(admin.ModelAdmin):
    list_display = ('cc_type', "code", "bank", 'country', 'purchased', 'date_created')
    list_filter = ('cc_type', "code", "bank", 'country', 'purchased', 'date_created')
    search_fields = ('code', "bank", 'country', 'cc_type')
    ordering = ('-date_created',)   