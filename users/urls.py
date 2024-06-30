from django.urls import path
from .views import CustomSignupView, profile_setup, profile_view, profile_edit


urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('profile/setup/', profile_setup, name='profile_setup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]
