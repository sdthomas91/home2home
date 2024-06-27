from django.db import models
from users.models import User

class Amenity(models.Model):
    name = models.CharField(max_length=50)
    # include font-awesome icons inspired by Isabella Mitchell Lonely House
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='properties'
        )
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    # Include lat & long for map display
    latitude = models.FloatField()
    longitude = models.FloatField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    amenities = models.ManyToManyField(Amenity, blank=True)
    # add pets_allowed to model for guests to set when adding property
    pets_allowed = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
        )
    image = models.ImageField(upload_to='property_images/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.property.title + " Image"
