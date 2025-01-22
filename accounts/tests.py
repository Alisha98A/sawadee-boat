from django.test import TestCase
from datetime import date, timedelta
from .forms import ProfileForm

# Create your tests here.
class ProfileFormTests(TestCase):
    def test_valid_data(self):
        form = ProfileForm(data={
            'birth_date': '2000-01-01',
            'phone_number': '+1234567890',
            'address': '123 Main St.'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_birth_date(self):
        form = ProfileForm(data={
            'birth_date': date.today().isoformat(),
            'phone_number': '+1234567890',
            'address': '123 Main St.'
        })
        self.assertFalse(form.is_valid())

    def test_invalid_phone_number(self):
        form = ProfileForm(data={
            'birth_date': '2000-01-01',
            'phone_number': '12345',
            'address': '123 Main St.'
        })
        self.assertFalse(form.is_valid())

    def test_invalid_address(self):
        form = ProfileForm(data={
            'birth_date': '2000-01-01',
            'phone_number': '+1234567890',
            'address': '$Invalid Address'
        })
        self.assertFalse(form.is_valid())