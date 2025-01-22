from django.core.exceptions import ValidationError

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