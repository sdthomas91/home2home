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
                user=request.user,
                property=property,
                checkin=form.cleaned_data['checkin'],
                checkout=form.cleaned_data['checkout'],
                guests=form.cleaned_data['guests'],
            )
            # Save the booking to trigger the save method in the model
            booking.save()
            messages.success(
                request,
                'Your dates are available! Please proceed to checkout'
            )
            return redirect('basket')
    else:
        form = BookingForm()
    return render(
        request,
        'properties/property_detail.html',
        {'property': property, 'form': form}
    )


@login_required
def basket_view(request):
    bookings = Booking.objects.filter(user=request.user)
    subtotal = sum(booking.total_price for booking in bookings)
    return render(request, 'bookings/basket.html', {'bookings': bookings, 'subtotal': subtotal})

