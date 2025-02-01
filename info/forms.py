from django import forms
from .models import Menu


# -------------------------------------
# Forms for Menu Management
# -------------------------------------
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "description", "is_active"]