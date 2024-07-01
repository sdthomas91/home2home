from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from properties.models import Property
from .forms import ReviewForm
from bookings.models import Booking

@login_required
def write_review(request, property_id):
    """
    View for users to leave reviews on properties in which they have stayed
    """
    property = get_object_or_404(Property, id=property_id)
    if not Booking.objects.filter(user=request.user, property=property).exists():
        messages.error(request, "You haven't stayed here yet, book now to leave a review!")
        return redirect('property_detail', property_id=property_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.guest = request.user
            review.property = property
            review.save()
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('property_detail', property_id=property_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/write_review.html', {'form': form, 'property': property})

@login_required
def property_reviews(request, property_id):
    """
    View for displaying reviews
    """
    property = get_object_or_404(Property, id=property_id)
    reviews = property.reviews.all()
    return render(request, 'reviews/property_reviews.html', {'property': property, 'reviews': reviews})
