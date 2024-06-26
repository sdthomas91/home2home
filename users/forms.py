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


class GuestSignupForm(SignupForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)

    def save(self, request):
        user = super(GuestSignupForm, self).save(request)
        user.profile.user_type = 'Guest'
        user.profile.bio = self.cleaned_data.get('bio')
        user.profile.save()
        return user

class HostSignupForm(SignupForm):
    bio = forms.CharField(required=True, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=True)

    def save(self, request):
        user = super(HostSignupForm, self).save(request)
        user.profile.user_type = 'Host'
        user.profile.bio = self.cleaned_data.get('bio')
        user.profile.profile_picture = self.cleaned_data.get('profile_picture')
        user.profile.save()
        return user
