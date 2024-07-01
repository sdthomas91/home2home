from django.urls import path
from .views import write_review, property_reviews

urlpatterns = [
    path('write_review/<int:property_id>/', write_review, name='write_review'),
]
