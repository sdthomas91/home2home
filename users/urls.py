from django.urls import path
from .views import CustomSignupView, profile_setup

urlpatterns = [
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('profile/setup/', profile_setup, name='profile_setup'),
]
