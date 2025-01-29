from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Reservation

class BaseReservationForm(forms.ModelForm):
    """
    Base reservation form containing common fields for both users and staff.
    """
    pass