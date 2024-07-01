from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
from django.db.models import Avg
from django.utils import timezone

class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
        )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='reviews'
        )
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='host_reviews'
        )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review: {self.guest.username} - {self.property.title}"

    def save(self, *args, **kwargs):
        self.host = self.property.host
        super().save(*args, **kwargs)
        self.property.update_average_rating()
