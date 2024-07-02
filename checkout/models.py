from django.db import models
from properties.models import Property
from bookings.models import Booking
from django.contrib.auth.models import User


class Order(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for Booking {self.booking.id}"