from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance')
    list_filter = ('username', 'balance')
    search_fields = ('username',)
    ordering = ('id',)