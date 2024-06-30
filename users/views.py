from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomSignupForm, GuestProfileForm, HostProfileForm, ProfileEditForm
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from .models import Profile


class CustomSignupView(SignupView):
    """
    Provides a custom signup form to allow users to select
    their status as a host or a guest inc. a redirect on signup so they 
    can complete the relevant profile setup
    """
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('profile_setup')


@login_required
def profile_setup(request):
    """
    Display the profile setup that allows users to complete setting up their
    profile following signup. Displays different fields depending on status
    Guest or Host
    """
    if request.user.profile.user_type == 'Host':
        form = HostProfileForm(instance=request.user.profile)
    else:
        form = GuestProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        if request.user.profile.user_type == 'Host':
            form = HostProfileForm(request.POST, instance=request.user.profile)
        else:
            form = GuestProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'users/profile_setup.html', {'form': form})





@login_required
def profile_view(request):
    """
    Loads the profile page for viewing
    """
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    """
    Loads the profile page for editing
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form, 'profile': profile})
