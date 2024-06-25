from django.db import models

# Create your models here.


class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True)
    bio = models.TextField()
    join_date = models.DateField()
    interests = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.name

    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return '/media/no_profile_pic.jpg'