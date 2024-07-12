from django.shortcuts import render
from properties.models import Property
from reviews.models import Review
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


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


def test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django using Gmail.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['samueldthomas91@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully')
