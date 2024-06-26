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
    if request.user.profile.user_type == 'Guest':
        form_class = GuestProfileForm
    else:
        form_class = HostProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = form_class(instance=request.user.profile)

    return render(request, 'account/profile_setup.html', {'form': form})


@login_required
def profile_view(request):
    """
    Loads the profile page for viewing and editing 
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'profile': profile})

