from django.test import TestCase
from info.forms import MenuForm


class TestMenuForm(TestCase):
    
    def test_menu_form_is_valid(self):
        form = MenuForm({'name': 'Lunch Menu', 'description': 'A delicious lunch menu', 'is_active': True})
        self.assertTrue(form.is_valid(), msg="MenuForm should be valid")

    def test_menu_form_is_invalid(self):
        form = MenuForm({'name': '', 'description': 'No name provided', 'is_active': True})
        self.assertFalse(form.is_valid(), msg="MenuForm should be invalid due to missing name")
