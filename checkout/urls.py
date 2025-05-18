from django.urls import path
from .views import CreateCheckoutSessionView

urlpatterns = [
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
]