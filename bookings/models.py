from django.db import models
from django.contrib.auth.models import User
from properties.models import Property

class Booking(models.Model):
    """
    Booking model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
        )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking {self.id} - {
            self.property.title
            } by {self.user.username}'


from django.db import models
from django.contrib.auth.models import User
from properties.models import Property

class Basket(models.Model):
    """
    Basket model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Basket Item {self.id} - {self.property.title} by {self.user.username}'
