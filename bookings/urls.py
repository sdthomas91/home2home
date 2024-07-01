from django.urls import path
from .views import book_property, basket_view

urlpatterns = [
    path('book/<int:property_id>/', book_property, name='book_property'),
    path('basket/', basket_view, name='basket'),  # Add this line for the basket view
]
