from django.db import models
from properties.models import Property
from django.contrib.auth.models import User
# https://www.geeksforgeeks.org/python-datetime-timedelta-function/
from datetime import timedelta

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()
    nights = models.IntegerField(editable=False, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0.0)

    def save(self, *args, **kwargs):
        if isinstance(self.checkin, str):
            self.checkin = datetime.strptime(self.checkin, "%Y-%m-%d").date()
        if isinstance(self.checkout, str):
            self.checkout = datetime.strptime(self.checkout, "%Y-%m-%d").date()
        # Calculate the number of nights
        self.nights = (self.checkout - self.checkin).days
        # Calculate the total price
        self.total_price = self.nights * self.property.price_per_night
        super().save(*args, **kwargs)
