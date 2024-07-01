from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from users.models import User
# Star ratings found 
# https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
from star_ratings.models import Rating


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    # for font-awesome icons inspired by Isabella Mitchell Lonely House
    font_awesome_class = models.CharField(max_length=50)
    # Custom ordering to prioritise most popular amenities
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Amenity")
        verbose_name_plural = _("Amenities")
        ordering = ['order', 'name']


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
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    amenities = models.ManyToManyField(Amenity, blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def update_average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.average_rating = avg_rating
        self.save()

    def render_star_rating(self):
        if not self.average_rating:
            return format_html('<span class="text-info">No Ratings Yet</span>')
        
        filled_stars = int(self.average_rating)
        empty_stars = 5 - filled_stars
        half_star = 1 if self.average_rating - filled_stars >= 0.5 else 0
        
        stars_html = ''.join(['<i class="fa-solid fa-star"></i>' for _ in range(filled_stars)])
        stars_html += ''.join(['<i class="fa-regular fa-star"></i>' for _ in range(empty_stars - half_star)])
        if half_star:
            stars_html += '<i class="fa-solid fa-star-half-alt"></i>'
        
        return format_html(stars_html)

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
