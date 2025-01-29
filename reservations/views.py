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


class ReservationListView(ListView):
    queryset = Reservation.objects.filter(booking_date__gte=date.today()).order_by('booking_date', 'time_slot')
    template_name = 'reservations/reservation_list.html'  
    context_object_name = 'reservations'