from django.urls import path
from .views import CustomSignupView, profile_setup, profile_view, address_edit, profile_edit, my_properties

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('profile/setup/', profile_setup, name='profile_setup'),
    path('profile/', profile_view, name='profile'),
    path('profile/address_edit/', address_edit, name='address_edit'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('my_properties/', my_properties, name='my_properties'),
]
