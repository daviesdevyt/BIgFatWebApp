from django.contrib import admin
from .models import News, CC, Fullz, Logs, Guides, Services, Dumps, Order, CCBase

# Register your models here.
admin.site.register(News)
admin.site.register(CC)
admin.site.register(Fullz)
admin.site.register(Logs)
admin.site.register(Guides)
admin.site.register(Services)
admin.site.register(CCBase)
admin.site.register(Dumps)