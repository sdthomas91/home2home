# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomSignupForm, GuestProfileSetupForm, HostProfileSetupForm, ProfileEditForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from .models import Profile

class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('profile_setup')

@login_required
def profile_setup(request):
    if request.user.profile.user_type == 'Host':
        form = HostProfileSetupForm(instance=request.user.profile)
    else:
        form = GuestProfileSetupForm(instance=request.user.profile)

    if request.method == 'POST':
        if request.user.profile.user_type == 'Host':
            form = HostProfileSetupForm(request.POST, request.FILES, instance=request.user.profile)
        else:
            form = GuestProfileSetupForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'users/profile_setup.html', {'form': form})

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def address_edit(request):
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
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'users/profile_edit.html', {'form': form})