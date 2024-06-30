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
        exclude = ['host', 'featured']  # Exclude host to handle it in the view

    def __init__(self, *args, **kwargs):
        super(PropertyCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']