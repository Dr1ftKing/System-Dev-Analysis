from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomSignupForm
# from django.shortcuts import render

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

def register(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.user_type = form.cleaned_data['user_type']
            user.profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'core/register.html', {'form': form})

