from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from allauth.account.views import PasswordChangeView
from .models import Profile
from .forms import ProfileForm


# -------------------------
# Profile Views & Update
# -------------------------
@login_required
def profile_view(request):
    """Display the user's profile."""
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile

# -------------------------
# Authentication Views
# -------------------------
def signup(request):
    """Handle user registration."""
    form = CustomSignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(request)
        return redirect('success')
    return render(request, 'accounts/signup.html', {'form': form})


class CustomPasswordChangeView(PasswordChangeView):
    """Allow users to change their password with success/error messages."""
    def form_valid(self, form):
        messages.success(self.request, "Your password has been changed successfully.")
        return redirect('account_profile')

    def form_invalid(self, form):
        messages.error(self.request, "There was an error changing your password. Please try again.")
        return super().form_invalid(form)