from django.db import models


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
