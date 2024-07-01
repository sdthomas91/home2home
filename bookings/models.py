from django.db import models
from django.contrib.auth.models import User
from properties.models import Property

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f'Booking by {self.user.username} for {self.property.title}'
