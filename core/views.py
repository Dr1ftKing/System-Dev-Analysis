from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def features(request):
    return render(request, 'core/features.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def contact(request):
    return render(request, 'core/contact.html')

def booking(request):
    return render(request, 'core/booking.html')
