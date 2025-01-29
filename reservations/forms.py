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

    booking_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'required': True}),
        error_messages={"required": "Please select a booking date."}
    )

    time_slot = forms.ChoiceField(
        choices=TIME_SLOTS,
        required=True,
        error_messages={"required": "Please select a time slot."}
    )

    number_of_guests = forms.ChoiceField(
        choices=GUEST_CHOICES,
        required=True,
        error_messages={"required": "Please select the number of guests."}
    )

    class Meta:
        model = Reservation
        fields = [
            'booking_date', 'time_slot', 'number_of_guests',
            'first_name', 'last_name', 'phone_number', 'email_address'
        ]