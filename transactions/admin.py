from django.contrib import admin
from base.models import Order
from .models import Transaction
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', "product", 'date_created', "view_product")
    list_filter = ('user', 'product', 'date_created')
    search_fields = ("product_id", 'user', 'product')
    ordering = ('-date_created',)

    def view_product(self, obj):
        detail_url = "/admin/base/{}/{}/change/".format(obj.product, obj.product_id)
        return format_html('<a href="{}">View product</a>', detail_url)

@admin.register(Transaction)
class TransacrtionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'pay_id', 'status', 'user', 'date_created')
    list_filter = ('amount', 'pay_id', 'status', 'user', 'date_created')
    search_fields = ('amount', 'pay_id', 'status', 'user')
    ordering = ('-date_created',)
    