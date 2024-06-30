from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['name'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.DEFAULT_FROM_EMAIL],
            )
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
