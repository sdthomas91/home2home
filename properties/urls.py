from django.urls import path
from .views import all_properties, property_detail, add_property, edit_property, search_results, manage_properties, superuser_edit_property

urlpatterns = [
    path('properties/', all_properties, name='all_properties'),
    path('properties/<int:property_id>/', property_detail, name='property_detail'),
    path('properties/add/', add_property, name='add_property'),
    path('edit/<int:property_id>/', edit_property, name='edit_property'),
    path('property/delete/<int:property_id>/', delete_property, name='delete_property'),
    path('search/', search_results, name='search_results'),
    path('manage_properties/', manage_properties, name='manage_properties'),
    path('superuser_edit/<int:property_id>/', superuser_edit_property, name='superuser_edit_property'),
]
