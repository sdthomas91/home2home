from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookings.models import Booking
from .models import Order, PaymentDetail
from .forms import CheckoutForm
import stripe

stripe.api_key = 'sk_test_51PY2bgFil8lo0gUPG6SZWjsEclPb6fLyu8noaxB9KDSChxHRrjqxizRu6CiSQ6qJr5ZQyWgzOVBb9aNqLyyScdqr00KvWJSxk7'

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

                # Create order
                for booking in bookings:
                    Order.objects.create(
                        booking=booking,
                        user=user,
                        total_price=total_price,
                        payment_status='Paid',
                        street_address1=form.cleaned_data['street_address1'],
                        street_address2=form.cleaned_data['street_address2'],
                        town_or_city=form.cleaned_data['town_or_city'],
                        county=form.cleaned_data['county'],
                        country=form.cleaned_data['country'],
                        postcode=form.cleaned_data['postcode']
                    )

                # Save payment details if the user opted to
                if form.cleaned_data['save_payment_details']:
                    PaymentDetail.objects.create(
                        user=user,
                        card_number=form.cleaned_data['card_number'],
                        expiry_date=form.cleaned_data['expiry_date'],
                        cvv=form.cleaned_data['cvv']
                    )

                messages.success(request, "Payment successful and booking confirmed!")
                return redirect('my_bookings')
            except stripe.error.CardError as e:
                messages.error(request, f"Payment error: {e.error.message}")
                return redirect('checkout')

    return render(
        request,
        'checkout/checkout.html',
        {
            'bookings': bookings,
            'total_price': total_price,
            'form': form
        }
    )
