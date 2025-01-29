from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Reservation
from .forms import ReservationFormForUser, ReservationFormForStaff
from datetime import date

# ---------------------------------
# View & Create Reservation
# ---------------------------------

@login_required
def reservation_view(request):
    """
    Handles reservation form for users and staff.
    Staff can create a reservation for any user, while normal users can only create their own reservations.
    """
    form_class = ReservationFormForStaff if request.user.is_staff else ReservationFormForUser
    form = form_class(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation successfully created!")
            return redirect("reservation_success")
        else:
            messages.error(request, "Please correct the errors below.")

    return render(
        request, "reservation_form.html",
        {"form": form, "user_type": "staff" if request.user.is_staff else "guest"}
    )

@login_required
def reservation_success(request):
    """Displays a success page after creating a reservation."""
    return render(request, "reservation_success.html")


# ---------------------------------
# List of Reservations
# ---------------------------------

class ReservationListView(LoginRequiredMixin, ListView):
    """
    Displays a list of reservations.
    - Staff: See all reservations.
    - Users: See only their own reservations.
    """
    model = Reservation
    template_name = "reservation_list.html"
    context_object_name = "reservations"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Reservation.objects.all().order_by("booking_date", "time_slot")
        return Reservation.objects.filter(user=self.request.user).order_by("booking_date")


# ---------------------------------
# Staff Dashboard
# ---------------------------------

class StaffDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    Dashboard view for staff to manage all reservations.
    Only staff members can access this page.
    """
    model = Reservation
    template_name = "staff_dashboard.html"
    context_object_name = "reservations"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        return redirect("reservation_list")

    def get_queryset(self):
        return Reservation.objects.all().order_by("booking_date")


# ---------------------------------
# Create Reservation
# ---------------------------------

class ReservationCreateView(LoginRequiredMixin, CreateView):
    """
    Handles creating a reservation.
    - Users can only create their own reservations.
    - Staff must select a user when creating a reservation.
    """
    model = Reservation
    template_name = "reservations/reservation_form.html"
    success_url = reverse_lazy("reservation_list")

    def get_form_class(self):
        return ReservationFormForStaff if self.request.user.is_staff else ReservationFormForUser

    def form_valid(self, form):
        reservation = form.save(commit=False)

        if self.request.user.is_staff:
            # Ensure staff selects a user
            if not form.cleaned_data.get("user"):
                messages.error(self.request, "Staff must select a user for the reservation.")
                return self.form_invalid(form)
            reservation.user = form.cleaned_data["user"]
        else:
            reservation.user = self.request.user

        # Track the creator of the reservation
        reservation.created_by = self.request.user
        reservation.save()

        messages.success(self.request, "Reservation successfully created!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There were errors in your submission. Please check your inputs.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("reservations:reservations_list")