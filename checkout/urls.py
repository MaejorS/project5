from django.urls import path
from .views import CreateCheckoutSessionView, OrderSuccessView
from . import views

urlpatterns = [
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('order-success/<int:pk>/', OrderSuccessView.as_view(), name='order_success'),
    path('my-profile/', views.customer_profile_view, name='customer_profile'),
]