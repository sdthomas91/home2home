from allauth.account.forms import SignupForm
from django import forms

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
