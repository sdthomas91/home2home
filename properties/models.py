from django.db import models

# Create your models here.

from django.db import models
from hosts.models import Host

class Property(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
        )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
        )
    property_type = models.CharField(max_length=50, choices=[
        ('Apartment', 'Apartment'),
        ('Cottage', 'Cottage'),
        ('Villa', 'Villa'),
        ('House', 'House'),
        ('Loft', 'Loft'),
        ('Flat', 'Flat')
    ])
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    amenities = models.TextField()  # change to amenity model
    images = models.ImageField(
        upload_to='property_images/',
        null=True,
        blank=True
        )
    availability_calendar = models.TextField()  # consider a booking model

    def __str__(self):
        return self.title