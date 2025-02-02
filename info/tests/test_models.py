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


class TestItemModel(TestCase):
    """Tests for the Item model."""

    def setUp(self):
        """Set up test menu, menu item, and item."""
        self.menu = Menu.objects.create(name="Breakfast Menu")
        self.menu_item = MenuItem.objects.create(menu=self.menu, category="Drinks")
        self.item = Item.objects.create(
            menu_item=self.menu_item,
            name="Orange Juice",
            description="Freshly squeezed orange juice",
            price=4.99
        )

    def test_item_str(self):
        """Test the string representation of the Item model."""
        self.assertEqual(str(self.item), "Orange Juice")

    def test_item_creation(self):
        """Test that an item can be created and retrieved."""
        item = Item.objects.get(name="Orange Juice")
        self.assertEqual(item.description, "Freshly squeezed orange juice")
        self.assertEqual(float(item.price), 4.99)

    def test_item_foreign_key(self):
        """Test that an item is correctly related to a menu item."""
        self.assertEqual(self.item.menu_item.category, "Drinks")
        self.assertEqual(self.item.menu_item.menu.name, "Breakfast Menu")