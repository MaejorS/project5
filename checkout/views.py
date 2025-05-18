from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from products.models import Product
from django.views import View
from django.http import JsonResponse
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get("pk")
        product = get_object_or_404(Product, pk=product_id)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product.price * 100),  # price in cents
                    'product_data': {
                        'name': product.name,
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('order_success', args=[product.id])
            ),
            cancel_url=request.build_absolute_uri('/') + '?canceled=true',
        )

        return redirect(session.url, code=303)

@method_decorator(login_required, name='dispatch')
class OrderSuccessView(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("pk")
        product = get_object_or_404(Product, pk=product_id)
        
        Order.objects.create(
            user=request.user,
            product=product,
            price_paid=product.price,
            stripe_payment_id="test_payment_id"
        )

        from django.contrib import messages
        messages.success(request, f"Order placed for {product.name}! Please pickup your order with The Operations Admin!")
        return redirect('home')
