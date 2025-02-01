from django import forms
from .models import Menu, MenuItem

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
