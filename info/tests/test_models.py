from django.test import TestCase
from info.models import Menu, MenuItem, Item


class TestMenuModel(TestCase):
    """Tests for the Menu model."""

    def setUp(self):
        """Set up a test menu."""
        self.menu = Menu.objects.create(
            name="Dinner Menu",
            description="A delicious dinner selection.",
            is_active=True
        )

    def test_menu_str(self):
        """Test the string representation of the Menu model."""
        self.assertEqual(str(self.menu), "Dinner Menu")

    def test_menu_creation(self):
        """Test that a menu can be created and retrieved."""
        menu = Menu.objects.get(name="Dinner Menu")
        self.assertEqual(menu.description, "A delicious dinner selection.")
        self.assertTrue(menu.is_active)


class TestMenuItemModel(TestCase):
    """Tests for the MenuItem model."""

    def setUp(self):
        """Set up test menu and menu items."""
        self.menu = Menu.objects.create(name="Lunch Menu")
        self.menu_item = MenuItem.objects.create(menu=self.menu, category="Appetizers")

    def test_menu_item_str(self):
        """Test the string representation of the MenuItem model."""
        self.assertEqual(str(self.menu_item), "Lunch Menu - Appetizers")

    def test_menu_item_creation(self):
        """Test that a menu item can be created and retrieved."""
        menu_item = MenuItem.objects.get(category="Appetizers")
        self.assertEqual(menu_item.menu.name, "Lunch Menu")