from django.urls import path
from .views import all_properties, property_detail, add_property, edit_property

urlpatterns = [
    path('properties/', all_properties, name='all_properties'),
    path('properties/<int:property_id>/', property_detail, name='property_detail'),
    path('properties/add/', add_property, name='add_property'),
    path('edit/<int:property_id>/', edit_property, name='edit_property'),
]
