from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    if request.GET.get('success') == 'true':
        messages.success(request, "Order placed successfully!")

    if request.GET.get('canceled') == 'true':
        messages.warning(request, "Payment was canceled.")

def index(request):
    """A view to return the index page"""
    
    return render(request, 'home/index.html')