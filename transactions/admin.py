from django.contrib import admin
from base.models import Order
from .models import Transaction

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', "product", 'date_created')
    list_filter = ('user', 'product', 'date_created')
    search_fields = ('user', 'product')
    ordering = ('-date_created',)

@admin.register(Transaction)
class TransacrtionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'pay_id', 'status', 'user', 'date_created')
    list_filter = ('amount', 'pay_id', 'status', 'user', 'date_created')
    search_fields = ('amount', 'pay_id', 'status', 'user')
    ordering = ('-date_created',)
    