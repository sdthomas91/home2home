from django.urls import path
from .views import all_properties

urlpatterns = [
    path('properties/', all_properties, name='all_properties'),
]
