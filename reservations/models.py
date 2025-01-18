from datetime import timedelta, datetime, date
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Boat(models.Model):
    """
    The Boat model represents a dining boat used for reservations.
    It stores information about the boat's name, description, and capacity.
    This model is used to keep track of available boats for customer bookings.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()  
    capacity = models.IntegerField()  

    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    """
    The Reservation model represents a booking made by a user for a specific boat.
    It stores the user who made the reservation, the boat being reserved, the booking date, 
    the time slot, and the number of guests. It also includes an optional discount field.
    The model ensures that the number of guests is between 4 and 20 through the clean method.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)  
    booking_date = models.DateField()  
    time_slot = models.TimeField()  
    number_of_guests = models.IntegerField() 
    has_discount = models.BooleanField(default=False, null=True, blank=True) 

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.booking_date}"

    def clean(self):
        """Validates the reservation details, including time slots, guest limits, and overlaps."""
        today = date.today()

        # Prevent past bookings and enforce 2-day advance notice
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