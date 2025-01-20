from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from .models import Reservation
from datetime import date

# Create your views here.
class ReservationListView(ListView):
    queryset = Reservation.objects.filter(booking_date__gte=date.today()).order_by('booking_date', 'time_slot')
    template_name = 'reservations/reservation_list.html'  
    context_object_name = 'reservations'