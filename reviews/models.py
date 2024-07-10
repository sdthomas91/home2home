from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


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

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.property.update_average_rating()


@receiver(post_save, sender=Review)
def update_property_rating_on_save(sender, instance, **kwargs):
    instance.property.update_average_rating()


@receiver(post_delete, sender=Review)
def update_property_rating_on_delete(sender, instance, **kwargs):
    instance.property.update_average_rating()
