import uuid
from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
from bookings.models import Booking
from users.models import Profile
from django.db.models import Sum

class Order(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True)
    user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    town_or_city = models.CharField(max_length=255)
    county = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total each time a line item is added,
        """
        self.total_price = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    property = models.ForeignKey(Property, null=False, blank=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, null=False, blank=False, default="Reservation")
    date = models.DateField(null=True, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.property.price_per_night * self.order.booking.total_nights
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.property.name} on order {self.order.order_number}'
