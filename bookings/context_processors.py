from .models import Booking

def basket_contents(request):
    basket_item = None
    total = 0

    if request.user.is_authenticated:
        booking = Booking.objects.filter(user=request.user, status='Pending').first()
        if booking:
            total = booking.total_price
            basket_item = booking

    return {
        'basket_item': basket_item,
        'total': total,
    }