# checkout/admin.py
from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'created_at', 'total_price', 'stripe_pid',
    )

    fields = ('order_number', 'user_profile', 'created_at',
              'first_name', 'last_name', 'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city',
              'county', 'country', 'postcode', 'total_price',
              'stripe_pid')

    list_display = ('order_number', 'created_at', 'first_name', 'last_name', 'total_price',)

    ordering = ('-created_at',)

admin.site.register(Order, OrderAdmin)
