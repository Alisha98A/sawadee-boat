from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Profile

def validate_phone_number(value):
    """
    Custom validator for phone number:
    - Removes non-digit characters.
    - Ensures the phone number is between 9 and 15 digits.
    """
    cleaned_value = ''.join(filter(str.isdigit, value))

    # Ensure phone number length is within the valid range
    if len(cleaned_value) < 9 or len(cleaned_value) > 15:
        raise ValidationError("Phone number must be between 9 and 15 digits.")
    
    return cleaned_value

class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=15,  
        required=True,
        validators=[validate_phone_number] 
    )
    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'text', 'placeholder': 'YYYY-MM-DD'})
    )
    address = forms.CharField(
        max_length=255,
        required=False,
        help_text="Enter your full address."
    )

    class Meta:
        model = Profile
        fields = ['birth_date', 'phone_number', 'address']