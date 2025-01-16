from django.contrib import admin
from .models import Boat, Reservation

# Register your models here.
admin.site.register(Boat)
admin.site.register(Reservation)