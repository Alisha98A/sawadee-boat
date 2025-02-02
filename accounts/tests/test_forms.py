from django.test import TestCase
from accounts.forms import ProfileForm

class ProfileFormTest(TestCase):

    def test_valid_phone_number(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',  # Valid phone number
            'birth_date': '2000-01-01',
            'address': '123 Main St',
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())  # Should pass for valid phone number