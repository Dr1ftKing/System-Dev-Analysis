from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm , BookingForm
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


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'core/booking.html', {'form': form})

@login_required
def booking_list(request):
    if hasattr(request.user, 'profile') and request.user.profile.user_type == 'Cleaner':
        bookings = Booking.objects.filter(cleaner=request.user)
    else:
        bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'core/booking_list.html', {'bookings': bookings})