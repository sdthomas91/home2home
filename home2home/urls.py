from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from allauth.account.views import SignupView
from users.views import CustomSignupView
from .views import trigger_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('users.urls')),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'), 
    path('accounts/', include('allauth.urls')),
    path('', include('properties.urls')),
    path('contact/', include('contact.urls')),
    path('bookings/', include('bookings.urls')),
    path('reviews/', include('reviews.urls')),
    path('checkout/', include('checkout.urls')),
    path('trigger-error/', trigger_error, name='trigger_error'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
