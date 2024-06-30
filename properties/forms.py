from django import forms
from .models import Property, PropertyImage
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
    class Meta:
        model = Property
        exclude = ['host'] # Set manually in the view

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']