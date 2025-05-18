from django.contrib import admin
from .models import CustomerProfile, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'stripe_payment_id', 'price_paid', 'created_at')

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'department')
