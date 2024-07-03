from django.urls import path
from .views import checkout, create_payment_intent

urlpatterns = [
    path('', checkout, name='checkout'),
    path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
]
