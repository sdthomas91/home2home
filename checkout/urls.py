from django.urls import path
from .views import checkout

urlpatters = [
    path('checkout/', checkout, name='checkout'),
]