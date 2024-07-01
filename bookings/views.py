from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from properties.models import Property
from .forms import BookingForm
from .models import Booking

@login_required
def book_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = Booking(
                user=request.user.profile,
                property=property,
                checkin=form.cleaned_data['checkin'],
                checkout=form.cleaned_data['checkout'],
                guests=form.cleaned_data['guests'],
            )
            booking.save()
            messages.success(request, 'Your booking was successfully created!')
            return redirect('checkout')
    else:
        form = BookingForm()
    return render(request, 'properties/property_detail.html', {'property': property, 'form': form})
