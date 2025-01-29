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