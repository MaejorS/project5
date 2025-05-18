from django.contrib import admin
from .models import Order
from django.utils.timezone import localtime

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'stripe_payment_id', 'created_time')
    
    def created_time(self, obj):
        return localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')

    created_time.short_description = 'Created At'
