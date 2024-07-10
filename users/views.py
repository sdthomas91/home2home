# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    CustomSignupForm, ProfileSetupForm, ProfileEditForm, AddressEditForm
    )
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from properties.models import Property


class CustomSignupView(SignupView):
    """
    A custom view that alters the standard allauth signup process to allow
    for custom forms
    """
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('profile_setup')


@login_required
def profile_setup(request):
    """
    A view for the original profile setup to which users are redirected after
    account creation
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileSetupForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileSetupForm(instance=profile)
    return render(request, 'users/profile_setup.html', {'form': form})


@login_required
def profile_edit(request):
    """
    A view allowing users to edit their profile information
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'users/profile_edit.html', {'form': form})


@login_required
def profile_view(request):
    """
    A view to display the logged in users profile
    """
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def address_edit(request):
    """
    A view to allow users to edit their address details separate to other
    profile info
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = AddressEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddressEditForm(instance=profile)
    return render(request, 'users/address_edit.html', {'form': form})


@login_required
def my_properties(request):
    """
    A view to render the properties page for the currently logged in host and
    to redirect logged out or "Guest" users
    """
    if request.user.profile.user_type != 'Host':
        messages.error(request, 'You must be a host to view this page.')
        return redirect('home')

    properties = Property.objects.filter(host=request.user)
    return render(
        request,
        'users/my_properties.html',
        {'properties': properties}
        )
