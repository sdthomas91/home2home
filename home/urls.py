from django.urls import path
from .views import home, test_email


urlpatterns = [
    path('', home, name='home'),
    path('test-email/', test_email, name='test_email'),
]
