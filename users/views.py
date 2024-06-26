from django.shortcuts import render, redirect
from .forms import CustomSignupForm, GuestProfileForm, HostProfileForm
from allauth.account.views import SignupView  #required to use allauth template
from django.contrib.auth.decorators import login_required


# Create your views here.

# Custom signup view
class CustomSignupView(SignupView):
    """
    Provides a custom signup form to allow users to select
    their status as a host or a guest inc. a redirect on signup so they 
    can complete the relevant profile setup
    """
    template_name = 'accounts/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('profile_setup')
