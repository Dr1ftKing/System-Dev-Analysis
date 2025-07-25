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

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    SERVICE_CHOICES = [
        ('Standard Cleaning', 'Standard Cleaning'),
        ('Deep Cleaning', 'Deep Cleaning'),
        ('Move-In/Out', 'Move-In/Out'),
    ]
    ADDONS_CHOICES = [
        ('Pet-Friendly Products', 'Pet-Friendly Products (+$10)'),
        ('Eco-friendly Supplies', 'Eco-friendly Supplies (+$5)'),
    ]

    service_type = forms.ChoiceField(choices=SERVICE_CHOICES, required=True, label="Service Type")
    add_ons = forms.MultipleChoiceField(
        choices=ADDONS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Optional Add-ons"
    )

    class Meta:
        model = Booking
        fields = ['cleaner', 'date', 'time', 'service_type', 'add_ons', 'notes']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cleaner'].queryset = User.objects.filter(profile__user_type='cleaner')

