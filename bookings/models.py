from django.db import models
from properties.models import Property
from django.contrib.auth.models import User
from datetime import datetime

class Booking(models.Model):
    # Add status so can add to my bookings
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()
    total_nights = models.IntegerField(editable=False, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        # Calculate the number of nights
        if isinstance(self.checkin, str):
            self.checkin = datetime.strptime(self.checkin, "%Y-%m-%d").date()
        if isinstance(self.checkout, str):
            self.checkout = datetime.strptime(self.checkout, "%Y-%m-%d").date()
            
        self.total_nights = (self.checkout - self.checkin).days
        self.total_price = self.total_nights * self.property.price_per_night

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Booking for {self.property.title} by {self.user.username}'