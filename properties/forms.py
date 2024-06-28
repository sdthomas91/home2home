from django import forms
from .models import Property
from users.models import Profile

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.fields['host'].queryset = Profile.objects.filter(user_type='Host').values_list('user', flat=True)
