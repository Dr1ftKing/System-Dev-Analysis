from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Booking
from .forms import CustomSignupForm , BookingForm
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
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

# def is_cleaner(user):
#     if not user.is_authenticated:
#         return False
#     try:
#         return user.profile.user_type == 'Cleaner'
#     except:
#         return False
def is_cleaner(user):
    print(f"Checking if user is cleaner: {user.username}")
    if not user.is_authenticated:
        print("User not authenticated")
        return False
    try:
        print(f"User type: {user.profile.user_type}")
        return user.profile.user_type == 'Cleaner'
    except Exception as e:
        print(f"Error checking user type: {e}")
        return False


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

@login_required
#@user_passes_test(is_cleaner)
def manage_bookings(request):
    bookings = Booking.objects.filter(status='Pending').order_by('date')
    return render(request, 'core/manage_bookings.html', {'bookings': bookings})


@login_required
@user_passes_test(is_cleaner)
@require_POST
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    status = request.POST.get('status')
    if status in ['Accepted', 'Rejected']:
        booking.status = status
        booking.save()
    return redirect('manage_bookings')
