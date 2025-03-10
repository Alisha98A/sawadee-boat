from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from allauth.account.views import PasswordChangeView
from django.utils.timezone import now
from .models import Profile
from .forms import ProfileForm
from reservations.models import Reservation


# -------------------------
# Profile Views & Update
# -------------------------
@login_required
def profile_view(request):
    """Display the user's profile with upcoming reservations."""
    profile, created = Profile.objects.get_or_create(user=request.user)

    upcoming_reservations = Reservation.objects.filter(
        user=request.user,
        booking_date__gte=now(),
    ).exists()

    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile,
            "has_upcoming_reservations": upcoming_reservations,
        },
    )


class ProfileUpdateView(UpdateView):
    """Allow users to update their profile."""
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user.profile


# -------------------------
# Authentication Views
# -------------------------
def signup(request):
    """Handle user registration."""
    form = CustomSignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save(request)
        return redirect("success")
    return render(request, "accounts/signup.html", {"form": form})


class CustomPasswordChangeView(PasswordChangeView):
    """Allow users to change their password with success/error messages."""

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your password has been changed successfully.",
        )
        return redirect("profile")

    def form_invalid(self, form):
        messages.error(
            self.request,
            "There was an error changing your password. Try again.",
        )
        return super().form_invalid(form)


# -------------------------
# Account Deletion View
# -------------------------
@login_required
def delete_account(request):
    """Allow users to delete their account with confirmation."""
    if request.method == "POST":
        messages.success(
            request,
            "Your account has been deleted successfully.",
        )
        user = request.user
        logout(request)
        user.delete()
        return redirect("account_login")

    return render(request, "accounts/delete_account.html")
