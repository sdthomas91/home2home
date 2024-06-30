from django import forms
from .models import Property, PropertyImage, Amenity
from users.models import Profile

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.fields[
            'host'
            ].queryset = Profile.objects.filter(
                user_type='Host'
                ).select_related('user')

        # Override the choices displayed in the dropdown
        self.fields['host'].queryset = Profile.objects.filter(user_type='Host')
        self.fields[
            'host'
            ].label_from_instance = lambda obj: f"{obj.user.username}"

class PropertyCreateForm(forms.ModelForm):
    amenities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Property
        exclude = ['host', 'featured', 'availability']

    def __init__(self, *args, **kwargs):
        super(PropertyCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['amenities'].widget.attrs['class'] = 'form-check-input'

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']