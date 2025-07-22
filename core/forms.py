from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Booking

class CustomSignupForm(UserCreationForm):
    USER_TYPES = [
        ('cleaner', 'Cleaner'),
        ('customer', 'Customer'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['cleaner', 'date', 'time', 'notes']
