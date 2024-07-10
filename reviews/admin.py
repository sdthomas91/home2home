from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('guest', 'property', 'rating', 'created_at')
    search_fields = ('guest__username', 'property__title', 'rating')
    list_filter = ('rating', 'created_at')
