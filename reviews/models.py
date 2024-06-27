from django.db import models
from users.models import User
from properties.models import Property

class Review(models.Model):
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
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review: {self.guest.username} - {self.property.title}"

    def save(self, *args, **kwargs):
        # automatically set host field based on the property reviewed
        self.host = self.property.host
        super().save(*args, **kwargs)
