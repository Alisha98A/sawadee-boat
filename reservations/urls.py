from django.urls import path
from . import views 
from .views import (
    ReservationListView,
    ReservationCreateView,
    ReservationUpdateView,
    ReservationDeleteView,
)

app_name = 'reservations' 

urlpatterns = [
    # Create reservation and success page
    path("reservations/create/", ReservationCreateView.as_view(), name="reservation_create"),

    # List view, edit and delete
    path("reservations/", ReservationListView.as_view(), name="reservations_list"),
    path("reservations/<int:pk>/edit/", ReservationUpdateView.as_view(), name="reservation_edit"),
    path("reservations/<int:pk>/delete/", ReservationDeleteView.as_view(), name="reservation_delete"),
]