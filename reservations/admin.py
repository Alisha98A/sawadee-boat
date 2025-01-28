from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for the Reservation model.
    """
    list_display = ('user', 'first_name', 'last_name', 'email_address', 'phone_number', 
                    'booking_date', 'time_slot', 'number_of_guests')
    list_filter = ('booking_date',)
    search_fields = ('user__username', 'first_name', 'last_name', 'email_address', 'phone_number')  
    ordering = ('booking_date', 'time_slot')
    date_hierarchy = 'booking_date'

    # This method will display the user's email in the admin
    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'