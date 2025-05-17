from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list_view(request):
    """Display a list of all products."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail_view(request, product_id):
    """Display a single product's detail view."""
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})