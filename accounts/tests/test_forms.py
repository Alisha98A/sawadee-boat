from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date
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

    def test_invalid_phone_number_length(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '123',  # Invalid phone number (too short)
            'birth_date': '2000-01-01',
            'address': '123 Main St',
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail
        self.assertEqual(form.errors['phone_number'], ['Phone number must be between 9 and 15 digits.'])

    def test_invalid_phone_number_non_digit(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '12a34567b890',  # Invalid phone number (contains non-digits)
            'birth_date': '2000-01-01',
            'address': '123 Main St',
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail
        self.assertEqual(form.errors['phone_number'], ['Phone number must only contain digits.'])

    def test_birth_date_in_future(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'birth_date': str(date.today().year + 1) + '-01-01',  # Future birthdate
            'address': '123 Main St',
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail
        self.assertEqual(form.errors['birth_date'], ['Birth date cannot be in the future.'])

    def test_underage_birth_date(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'birth_date': str(date.today().year - 17) + '-01-01',  # Underage
            'address': '123 Main St',
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail
        self.assertEqual(form.errors['birth_date'], ['You must be at least 18 years old.'])

    def test_valid_address(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'birth_date': '2000-01-01',
            'address': '123 Main St',  # Valid address
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())  # Should pass for valid address

    def test_invalid_address_characters(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'birth_date': '2000-01-01',
            'address': '123 Main $t',  # Invalid address (contains $)
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail
        self.assertEqual(form.errors['address'], ['Address contains invalid characters.'])