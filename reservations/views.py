from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Reservation
from .forms import ReservationFormForUser, ReservationFormForStaff
from datetime import date

# Create your views here.
class ReservationListView(ListView):
    queryset = Reservation.objects.filter(booking_date__gte=date.today()).order_by('booking_date', 'time_slot')
    template_name = 'reservations/reservation_list.html'  
    context_object_name = 'reservations'