from django.db import models
from cloudinary.models import CloudinaryField

# -------------------------------------
# Menu Model
# -------------------------------------
class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Menus"

# -------------------------------------
# MenuItem Model
# -------------------------------------
class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="items")
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.menu.name} - {self.category}"

# -------------------------------------
# Item Model
# -------------------------------------
class Item(models.Model):
    menu_item = models.ForeignKey("MenuItem", on_delete=models.CASCADE, related_name="menu_items")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # CloudinaryField with a default placeholder
    image = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return self.name