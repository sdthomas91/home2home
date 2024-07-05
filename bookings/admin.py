from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'checkin', 'checkout', 'guests', 'total_price', 'status')
    list_filter = ('status', 'checkin', 'checkout')
    search_fields = ('user__username', 'property__title')
    ordering = ('-checkin',)