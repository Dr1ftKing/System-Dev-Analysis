# core/admin.py
from django.contrib import admin
from .models import Profile, Booking

admin.site.register(Profile)
admin.site.register(Booking)
