from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('manage-bookings/', views.manage_bookings, name='manage_bookings'),
    path('update-booking-status/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
    path('register/', views.register, name='register'),
]
