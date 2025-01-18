from django.contrib import admin
from .models import Boat, Reservation

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for the Boat model.
    """
    list_display = ('name', 'capacity')
    search_fields = ('name',)

admin.site.register(Reservation)
