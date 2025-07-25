from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('cleaner', 'Cleaner'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    customer = models.ForeignKey(User, related_name='customer_bookings', on_delete=models.CASCADE)
    cleaner = models.ForeignKey(User, related_name='cleaner_bookings', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending'
    )

    service_type = models.CharField(max_length=50, blank=True, null=True)  # ✅ New
    add_ons = models.JSONField(blank=True, null=True)                      # ✅ New
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer.username} -> {self.cleaner.username} on {self.date}"

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)