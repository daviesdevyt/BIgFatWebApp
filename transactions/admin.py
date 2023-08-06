from django.contrib import admin
from base.models import Order
from .models import Transaction

# Register your models here.
admin.site.register(Order)
admin.site.register(Transaction)