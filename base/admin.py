from django.contrib import admin
from .models import News, CC, Fullz, Logs, Guides, Services, Dumps, Order, CCBase

# Register your models here.
admin.site.register(News)

@admin.register(CC)
class CCAdmin(admin.ModelAdmin):
    list_display = ('base', 'country', 'state', 'purchased', 'date_created')
    list_filter = ('base', 'country', 'state', 'purchased', 'date_created')
    search_fields = ('id', 'base', 'country', 'state')
    ordering = ('-date_created',)
    list_per_page = 25

@admin.register(Fullz)
class FullzAdmin(admin.ModelAdmin):
    list_display = ('category', 'country', 'purchased', 'date_created')
    list_filter = ('category', 'country', 'purchased', 'date_created')
    search_fields = ('id', 'base', 'country', 'state')
    ordering = ('-date_created',)

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('title', "category", 'purchased', 'date_created')
    list_filter = ('title', 'category', "purchased", 'date_created')
    search_fields = ('id', 'title', 'description', 'category')
    ordering = ('-date_created',)


@admin.register(Guides)
class GuidesAdmin(admin.ModelAdmin):
    list_display = ('title', "category", 'purchased', 'date_created')
    list_filter = ('title', 'category', "purchased", 'date_created')
    search_fields = ('id', 'title', 'description', 'category')
    ordering = ('-date_created',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', "category", 'purchased', 'date_created')
    list_filter = ('title', 'category', "purchased", 'date_created')
    search_fields = ('id', 'title', 'description', 'category')
    ordering = ('-date_created',)

@admin.register(CCBase)
class CCBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')
    list_filter = ('name', 'date_created')
    search_fields = ('name',)
    ordering = ('-date_created',)

@admin.register(Dumps)
class DumpsAdmin(admin.ModelAdmin):
    list_display = ('cc_type', "code", "bank", 'country', 'purchased', 'date_created')
    list_filter = ('cc_type', "code", "bank", 'country', 'purchased', 'date_created')
    search_fields = ('id', 'code', "bank", 'country', 'cc_type')
    ordering = ('-date_created',)   