from django.shortcuts import render
from properties.models import Property
from reviews.models import Review
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    featured_properties = Property.objects.filter(featured=True)[:4]
    latest_reviews = Review.objects.all()
    return render(
        request,
        'home/index.html',
        {
            'featured_properties': featured_properties,
            'latest_reviews': latest_reviews
        }
        )
