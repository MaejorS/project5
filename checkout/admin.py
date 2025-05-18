from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'stripe_payment_id', 'created_at')
    search_fields = ('user__username', 'product__name', 'stripe_payment_id')
    list_filter = ('created_at',)
