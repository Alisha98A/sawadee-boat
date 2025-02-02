from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from info.forms import MenuForm, MenuItemForm
from info.models import Menu, MenuItem
from PIL import Image
import io


class TestMenuForm(TestCase):
    
    def test_menu_form_is_valid(self):
        form = MenuForm({'name': 'Lunch Menu', 'description': 'A delicious lunch menu', 'is_active': True})
        self.assertTrue(form.is_valid(), msg="MenuForm should be valid")

    def test_menu_form_is_invalid(self):
        form = MenuForm({'name': '', 'description': 'No name provided', 'is_active': True})
        self.assertFalse(form.is_valid(), msg="MenuForm should be invalid due to missing name")


class TestMenuItemForm(TestCase):
    
    def setUp(self):
        """Create a menu instance for testing"""
        self.menu = Menu.objects.create(name="Test Menu", description="Test Description", is_active=True)

    def test_menu_item_form_is_valid(self):
        form = MenuItemForm({'menu': self.menu.id, 'category': 'Drinks'})
        self.assertTrue(form.is_valid(), msg="MenuItemForm should be valid")

    def test_menu_item_form_is_invalid(self):
        form = MenuItemForm({'menu': '', 'category': 'Desserts'})
        self.assertFalse(form.is_valid(), msg="MenuItemForm should be invalid due to missing menu")


class TestItemForm(TestCase):

    def setUp(self):
        """Create necessary instances for testing"""
        self.menu = Menu.objects.create(name="Dinner Menu", description="Tasty dinner menu", is_active=True)
        self.menu_item = MenuItem.objects.create(menu=self.menu, category="Main Course")

    def create_test_image(self):
        """Helper function to create a valid image file"""
        image_io = io.BytesIO()
        image = Image.new("RGB", (100, 100), color="red")
        image.save(image_io, format="JPEG")
        return SimpleUploadedFile("test.jpg", image_io.getvalue(), content_type="image/jpeg")