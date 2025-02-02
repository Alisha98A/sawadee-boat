from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from info.forms import MenuForm, MenuItemForm, ItemForm
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

    def test_item_form_is_valid(self):
        """Test valid ItemForm submission"""
        image_file = self.create_test_image()
        form = ItemForm(data={
            'menu_item': self.menu_item.id,
            'name': 'Spaghetti',
            'description': 'Delicious spaghetti with tomato sauce',
            'price': 15.99,
        }, files={'image': image_file})

        print("\nDebug - test_item_form_is_valid")
        print("Is form valid?:", form.is_valid())
        print("Form errors:", form.errors)

        self.assertTrue(form.is_valid(), msg=f"ItemForm should be valid but failed with errors: {form.errors}")

    def test_item_form_without_description(self):
        """Ensure item can be created without a description"""
        image_file = self.create_test_image()
        form = ItemForm(data={
            'menu_item': self.menu_item.id,
            'name': 'Pizza',
            'description': '',
            'price': 12.99,
        }, files={'image': image_file})

        print("\nDebug - test_item_form_without_description")
        print("Is form valid?:", form.is_valid())
        print("Form errors:", form.errors)

        self.assertTrue(form.is_valid(), msg=f"ItemForm should be valid even without a description, but errors: {form.errors}")

    def test_item_form_is_invalid_due_to_large_file(self):
        """Test that the form rejects large images"""
        large_image = SimpleUploadedFile("large.jpg", b"x" * (2 * 1024 * 1024 + 1), content_type="image/jpeg")
        form = ItemForm(data={
            'menu_item': self.menu_item.id,
            'name': 'Burger',
            'description': 'Juicy beef burger',
            'price': 10.99,
        }, files={'image': large_image})

        print("\nDebug - test_item_form_is_invalid_due_to_large_file")
        print("Is form valid?:", form.is_valid())
        print("Form errors:", form.errors)

        self.assertFalse(form.is_valid(), msg="ItemForm should be invalid due to large image size")