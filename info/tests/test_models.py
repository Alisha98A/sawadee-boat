from django.test import TestCase
from info.models import Menu


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