from allauth.account.forms import SignupForm
from django import forms
from .models import Profile

# custom signup form to include Guest or Host signup selection

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = (
        ('Host', 'Host'),
        ('Guest', 'Guest'),
    )
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.profile.user_type = self.cleaned_data.get('user_type')
        user.profile.save()
        return user


class GuestProfileForm(forms.ModelForm):
    full_name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    default_payment_method = forms.CharField(required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'default_payment_method', 'profile_picture']

class HostProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    bio = forms.CharField(widget=forms.Textarea)
    interests = forms.CharField(widget=forms.Textarea)
    hobbies = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ['first_name', 'address', 'bio', 'interests', 'hobbies']