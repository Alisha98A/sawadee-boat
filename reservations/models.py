from datetime import timedelta, datetime, date
from django.utils.timezone import make_aware
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.urls import reverse


class Reservation(models.Model):
    """
    The Reservation model represents a booking made by a user.
    It stores details like booking date, time slot, number of guests, and contact information.
    The model ensures guest limits, time slot validation, and prevents overlapping bookings.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    staff_member = models.ForeignKey(User, related_name='staff_reservations', null=True, blank=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="reservations_created")
    booking_date = models.DateField()  
    time_slot = models.TimeField()  
    number_of_guests = models.IntegerField() 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)   
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email_address = models.EmailField(validators=[EmailValidator()])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.booking_date}"

    def clean(self):
        """Validates the reservation details, including time slots, guest limits, and overlaps."""
        today = date.today()

        # **Booking Date Validation**
        if not self.booking_date:
            raise ValidationError("Booking date is required.")

        if self.booking_date < today:
            raise ValidationError("Booking date cannot be in the past.")
        
        if self.booking_date < today + timedelta(days=2):
            raise ValidationError("Bookings must be made at least 2 days in advance.")

        # Validate guest count
        if not 4 <= self.number_of_guests <= 20:
            raise ValidationError("Number of guests must be between 4 and 20.")

        # Validate time slot within operational hours
        opening_time = datetime.strptime("10:00", "%H:%M").time()
        closing_time = datetime.strptime("22:00", "%H:%M").time()
        if not opening_time <= self.time_slot <= closing_time:
            raise ValidationError("Bookings must be between 10:00 and 22:00.")

        # Ensure last booking starts by 20:00
        latest_start_time = datetime.strptime("20:00", "%H:%M").time()
        if self.time_slot > latest_start_time:
            raise ValidationError("Last booking must start at 20:00 or earlier.")

        # Prevent overlapping reservations
        start_time = make_aware(datetime.combine(self.booking_date, self.time_slot))
        end_time = start_time + timedelta(hours=2)
        overlapping_reservations = Reservation.objects.filter(
            booking_date=self.booking_date,
        ).exclude(id=self.id)

        for reservation in overlapping_reservations:
            existing_start = make_aware(datetime.combine(reservation.booking_date, reservation.time_slot))
            existing_end = existing_start + timedelta(hours=2)
            if start_time < existing_end and end_time > existing_start:
                raise ValidationError(
                    f"The boat is already booked from {existing_start.time()} to {existing_end.time()}."
                )


    def save(self, *args, **kwargs):
    # Ensure validation runs and assigns created_by before saving.
        if not self.id and not self.created_by: 
           self.created_by = self.created_by or self.user  
        self.clean()
        super().save(*args, **kwargs)