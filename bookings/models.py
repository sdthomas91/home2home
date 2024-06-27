from django.db import models
from users.models import User
from properties.models import Property

class Booking(models.Model):
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
        )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='bookings'
        )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking: {self.guest.username} - {self.property.title}"
