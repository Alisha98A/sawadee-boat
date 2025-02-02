from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from info.models import Menu, MenuItem, Item


class TestViews(TestCase):
    """Tests for the info app views."""

    def setUp(self):
        """Set up test data."""
        self.client = Client()

        # Create a normal user and a staff user
        self.user = get_user_model().objects.create_user(
            username="testuser", email="user@test.com", password="password123"
        )
        self.staff_user = get_user_model().objects.create_superuser(
            username="staffuser", email="staff@test.com", password="password123"
        )

        # Create a sample menu
        self.menu = Menu.objects.create(
            name="Test Menu", description="Sample menu description", is_active=True
        )

        # Create a menu item (category) associated with the menu
        self.menu_item = MenuItem.objects.create(
            menu=self.menu, category="Test Category"
        )

        # Create an item (dish) under the menu category with a valid Cloudinary placeholder
        self.item = Item.objects.create(
            menu_item=self.menu_item,
            name="Test Dish",
            description="Test Description",
            price=9.99,
            image="https://res.cloudinary.com/demo/image/upload/v1581091179/sample.jpg",
        )

    def test_home_view(self):
        """Test that the home page renders successfully."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/home.html")

    def test_about_view(self):
        """Test that the about page renders successfully."""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/about.html")

    def test_set_sail_view(self):
        """Test that the set sail page renders successfully."""
        response = self.client.get(reverse("set_sail"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/setsail.html")

    def test_menu_view(self):
        """Test that the menu page displays an active menu."""
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/menu.html")
        self.assertIn("menu", response.context)