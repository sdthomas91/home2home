# forms.py
from allauth.account.forms import SignupForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Row, Column
from .models import Profile

# Custom signup form to include Guest or Host signup selection
class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = (
        ('Host', 'Host'),
        ('Guest', 'Guest'),
    )
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="Are you a Host or Guest?")

    def save(self, request):
        user = super().save(request)
        user.profile.user_type = self.cleaned_data.get('user_type')
        user.profile.save()
        return user



class ProfileSetupForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    address_1 = forms.CharField(label="Address Line 1")
    address_2 = forms.CharField(label="Address Line 2", required=False)
    city = forms.CharField()
    state = forms.CharField()
    postal_code = forms.CharField(label="Postal Code")
    country = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)
    hobbies = forms.CharField(widget=forms.TextInput, required=False, label="Hobbies (comma separated)")
    interests = forms.CharField(widget=forms.TextInput, required=False, label="Interests (comma separated)")

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'postal_code',
            'country',
            'bio',
            'profile_picture',
            'hobbies',
            'interests'
        ]

# form for updating address
class AddressEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address_1',
            'address_2',
            'city',
            'state',
            'postal_code',
            'country'
        ]

# form for updating profile
class ProfileEditForm(forms.ModelForm):
    hobbies = forms.CharField(widget=forms.TextInput, required=False, label="Hobbies (comma separated)")
    interests = forms.CharField(widget=forms.TextInput, required=False, label="Interests (comma separated)")

    class Meta:
        model = Profile
        fields = [
            'bio',
            'hobbies',
            'interests',
            'profile_picture'
        ]
