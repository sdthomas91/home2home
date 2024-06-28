from django import forms
from django.contrib import admin
from users.models import User
from .models import Property, PropertyImage, Amenity

class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['host'].queryset = User.objects.filter(profile__user_type='Host')
        self.fields['host'].label_from_instance = lambda obj: f"{obj.username} ({obj.profile.bio})"

class PropertyImageInline(admin.StackedInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    inlines = [PropertyImageInline]
    list_display = ('title', 'host', 'city', 'country', 'price_per_night', 'featured')
    list_filter = ('city', 'country', 'featured')
    search_fields = ('title', 'host__username', 'city', 'country')

admin.site.register(Property, PropertyAdmin)

class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'font_awesome_class')

admin.site.register(Amenity, AmenityAdmin)
