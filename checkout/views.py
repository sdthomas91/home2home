# checkout/views.py

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from bookings.context_processors import basket_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from bookings.models import Booking
from users.models import Profile
import stripe
import json


stripe.api_key = settings.STRIPE_SECRET_KEY


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.PaymentIntent.modify(pid, metadata={
            'booking': json.dumps(
                list(Booking.objects.filter(user=request.user).values())
                ),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be processed right now.'
            'Please try again later.'
            )
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = basket_contents(request)
    booking = Booking.objects.filter(
        user=request.user, status='Pending'
        ).first()
    total = basket['total']

    if not booking:
        messages.error(request, "Your basket is empty.")
        return redirect('basket')

    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.total_price = total
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.booking = booking
            order.save()
            order_line_item = OrderLineItem(
                order=order,
                property=booking.property,
                type='Reservation',
                date=booking.checkin,
                lineitem_total=booking.total_price
            )
            order_line_item.save()

            booking.status = 'Confirmed'
            booking.save()

            messages.success(request, 'Checkout completed successfully!')
            return redirect(reverse('checkout_success', args=[order.id]))
        else:
            messages.error(
                request,
                'There was an error with your form.'
                'Please double-check your information.'
                )
    else:
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.first_name,
                    'last_name': profile.last_name,
                    'email': request.user.email,
                    'phone_number': profile.default_payment_method,
                    'country': profile.country,
                    'postcode': profile.postal_code,
                    'town_or_city': profile.city,
                    'street_address1': profile.address_1,
                    'street_address2': profile.address_2,
                    'county': profile.state,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            'Stripe public key is missing. Set it in the environment.'
            )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'subtotal': total,
        'bookings': [booking],  # Pass as a list for template compatibility
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_id):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, id=order_id)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_payment_method': order.phone_number,
                'country': order.country,
                'postal_code': order.postcode,
                'city': order.town_or_city,
                'address_1': order.street_address1,
                'address_2': order.street_address2,
                'state': order.county,
            }
            for key, value in profile_data.items():
                setattr(profile, key, value)
            profile.save()

    messages.success(
        request, f'Order successfully processed!'
        'Your order number is {order_id}.'
        'A confirmation email will be sent to {order.email}.'
    )

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
