from django.contrib import admin
from .models import Property, PropertyImage, Amenity
from .forms import PropertyForm

class PropertyImageInline(admin.StackedInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyForm
    inlines = [PropertyImageInline]
    list_display = ('title', 'host', 'city', 'country', 'price_per_night', 'featured')
    list_filter = ('city', 'country', 'featured')
    search_fields = ('title', 'host__username', 'city', 'country')

admin.site.register(Property, PropertyAdmin)

class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'font_awesome_class')

admin.site.register(Amenity, AmenityAdmin)
