from django.urls import path
from .views import CustomSignupView, profile_setup, profile_view
from . import views

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('profile/setup/', profile_setup, name='profile_setup'),
    path('profile/', profile_view, name='profile'),
]
