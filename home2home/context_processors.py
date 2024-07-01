from bookings.models import Booking

def basket_total(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        grand_total = sum(booking.total_price for booking in bookings)
    else:
        grand_total = 0
    return {'grand_total': grand_total}
