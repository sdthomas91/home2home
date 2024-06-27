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
    booking_status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')],
        default='Pending')
    #  https://www.geeksforgeeks.org/datefield-django-models/
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # capitalize the username for a nicer display
        return f"Booking: {
            self.guest.username.capitalize()
            } - {self.property.title}"
