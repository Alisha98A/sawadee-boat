from django import forms
from django.core.exceptions import ValidationError
from .models import Menu, MenuItem, Item

# -------------------------------------
# File Upload Validation
# -------------------------------------
def validate_image(file):
    """Ensure the uploaded file is an image and not too large."""
    max_size = 2 * 1024 * 1024
    valid_extensions = ["jpg", "jpeg", "png", "gif"]

    # Check file size
    if file.size > max_size:
        raise ValidationError(f"File size must be under 2MB. Your file is {file.size / (1024 * 1024):.2f}MB.")

    # Check file type
    ext = file.name.split(".")[-1].lower()
    if ext not in valid_extensions:
        raise ValidationError("Invalid file type. Only JPG, PNG, and GIF files are allowed.")

# -------------------------------------
# Forms for Menu Management
# -------------------------------------
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "description", "is_active"]

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["menu", "category"]

class ItemForm(forms.ModelForm):
    """Form for adding/editing menu items with image validation."""
    image = forms.ImageField(validators=[validate_image])

    class Meta:
        model = Item
        fields = ["menu_item", "name", "description", "price", "image"]