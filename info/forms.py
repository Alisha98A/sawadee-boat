from django import forms
from .models import Menu, MenuItem, Item


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