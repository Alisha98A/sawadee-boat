from django.contrib import admin
from .models import Boat, Reservation

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for the Boat model.
    """
    list_display = ('name', 'capacity')
    search_fields = ('name',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for the Reservation model.
    """
    list_display = ('user', 'user_email', 'boat', 'booking_date', 'time_slot', 'number_of_guests', 'has_discount')
    list_filter = ('booking_date', 'boat')
    search_fields = ('user__username', 'boat__name', 'user__email')  
    ordering = ('booking_date', 'time_slot')
    date_hierarchy = 'booking_date'