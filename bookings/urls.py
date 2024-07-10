from django.urls import path
from .views import (
    book_property, basket_view, delete_booking, clear_basket, my_bookings
    )


urlpatterns = [
    path('book/<int:property_id>/', book_property, name='book_property'),
    path('basket/', basket_view, name='basket'),
    path('delete/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('clear/', clear_basket, name='clear_basket'),
    path('my_bookings/', my_bookings, name='my_bookings'),
]
