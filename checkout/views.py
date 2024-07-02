from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookings.models import Booking
from .models import Order, PaymentDetail
from .forms import CheckoutForm
import stripe

stripe.api_key = 'sk_test_51PY2bgFil8lo0gUPG6SZWjsEclPb6fLyu8noaxB9KDSChxHRrjqxizRu6CiSQ6qJr5ZQyWgzOVBb9aNqLyyScdqr00KvWJSxk7'

# checkout/views.py
@login_required
def checkout(request):
    user = request.user
    bookings = Booking.objects.filter(user=user, total_price__gt=0)

    if not bookings.exists():
        messages.error(request, "Your basket is empty.")
        return redirect('basket')

    total_price = sum(booking.total_price for booking in bookings)
    form = CheckoutForm()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                stripe.Charge.create(
                    amount=int(total_price * 100),
                    currency="gbp",
                    source=request.POST['stripeToken'],
                    description="Booking charge",
                )

                # Mark bookings as confirmed
                bookings.update(confirmed=True)

                # Create an order record
                for booking in bookings:
                    Order.objects.create(
                        booking=booking,
                        total_price=total_price,
                        payment_status='Paid'
                    )
                messages.success(request, "Payment successful and booking confirmed!")
                return redirect('my_bookings')
            except stripe.error.CardError as e:
                messages.error(request, f"Payment error: {e.error.message}")
                return redirect('checkout')

    context = {
        'bookings': bookings,
        'total_price': total_price,
        'form': form,
        'stripe_public_key': 'pk_test_51PY2bgFil8lo0gUPDdftv8oVaMTbDir3Ott0fonwbNbh0HAl9HBrZED1L4A7Kprb68rZDM7ou3o0fWj76Co2f6lK00o7LeuxKw'
    }

    return render(request, 'checkout/checkout.html', context)

