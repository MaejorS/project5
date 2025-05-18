from django.shortcuts import render
from django.contrib import messages

def home(request):
    if request.GET.get('success') == 'true':
        messages.success(request, "Payment successful! Thanks for your purchase! Your device is ready for pickup with The Operations Admin.")
    elif request.GET.get('canceled') == 'true':
        messages.warning(request, "Payment canceled. Feel free to try again.")
    return render(request, 'home/index.html')