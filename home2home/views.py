# home2home/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def test_email(request):
    subject = 'Test Email'
    message = 'This is a test email.'
    recipient_list = ['your-email@example.com']  # Replace with your email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
    return render(request, 'test_email.html')
