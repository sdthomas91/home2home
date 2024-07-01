from django.urls import path
from .views import write_review, edit_review

urlpatterns = [
    path('write_review/<int:property_id>/', write_review, name='write_review'),
    path('edit_review/<int:review_id>/', edit_review, name='edit_review'),
]
