from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Property
from .forms import BookingForm

@login_required
def book_property(request, property_id):
    property = Property.objects.get(id=property_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.property = property
            booking.total_price = property.price_per_night * (booking.check_out - booking.check_in).days
            booking.save()
            return redirect('checkout', booking.id)
    else:
        form = BookingForm()
    return render(request, 'book_property.html', {'form': form, 'property': property})
