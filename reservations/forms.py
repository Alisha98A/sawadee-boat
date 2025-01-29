from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Reservation

class BaseReservationForm(forms.ModelForm):
    """
    Base reservation form containing common fields for both users and staff.
    """

    # Time slots for reservations
    TIME_SLOTS = [
        ('10-12', '10:00 - 12:00'),
        ('12-14', '12:00 - 14:00'),
        ('14-16', '14:00 - 16:00'),
        ('16-18', '16:00 - 18:00'),
        ('18-20', '18:00 - 20:00'),
        ('20-22', '20:00 - 22:00'),
    ]

    # Guest count choices (4-20 guests)
    GUEST_CHOICES = [(str(i), str(i)) for i in range(4, 21)]