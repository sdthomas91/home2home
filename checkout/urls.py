from django.urls import path
from .views import checkout, checkout_success, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('', checkout, name='checkout'),
    path(
        'checkout_success/<order_id>/',
        checkout_success,
        name='checkout_success'
        ),
    path(
        'cache_checkout_data/', cache_checkout_data, name='cache_checkout_data'
        ),
    path('wh/', webhook, name='webhook'),
]
]
