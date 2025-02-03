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

        # Create another menu (inactive)
        self.inactive_menu = Menu.objects.create(
            name="Inactive Menu", description="Not active", is_active=False
        )

        # Create a menu item (category) associated with the menu
        self.menu_item = MenuItem.objects.create(
            menu=self.menu, category="Test Category"
        )

        # Create an item (dish) under the menu category
        self.item = Item.objects.create(
            menu_item=self.menu_item,
            name="Test Dish",
            description="Test Description",
            price=9.99,
            image="https://res.cloudinary.com/demo/image/upload/v1581091179/sample.jpg",
        )

    # -------------------------------------
    #  Public Views Tests
    # -------------------------------------

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

    # -------------------------------------
    # Staff-Only Views Tests
    # -------------------------------------

    def test_staff_menu_requires_login(self):
        """Test that the staff menu is restricted to logged-in users."""
        response = self.client.get(reverse("staff_menu"))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_staff_menu_accessible_by_staff(self):
        """Test that the staff menu is accessible by staff users."""
        self.client.login(email="staff@test.com", password="password123")
        response = self.client.get(reverse("staff_menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/staff_menu.html")

    def test_add_menu_requires_staff(self):
        """Test that adding a menu is restricted to staff users."""
        response = self.client.post(reverse("add_menu"), {"name": "New Menu"})
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_edit_menu_requires_staff(self):
        """Test that editing a menu is restricted to staff users."""
        response = self.client.post(reverse("edit_menu", args=[self.menu.id]), {"name": "Updated Menu"})
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_add_menu_item_requires_staff(self):
        """Test that adding a menu category is restricted to staff users."""
        response = self.client.post(reverse("add_menu_item"), {"category": "New Category"})
        self.assertEqual(response.status_code, 302)

    def test_edit_menu_item_requires_staff(self):
        """Test that editing a menu category is restricted to staff users."""
        response = self.client.post(reverse("edit_menu_item", args=[self.menu_item.id]), {"category": "Updated Category"})
        self.assertEqual(response.status_code, 302)

    def test_add_item_requires_staff(self):
        """Test that adding a menu item is restricted to staff users."""
        response = self.client.post(reverse("add_item"), {
            "menu_item": self.menu_item.id,
            "name": "New Dish",
            "description": "New Description",
            "price": 12.99,
            "image": "https://res.cloudinary.com/demo/image/upload/v1581091179/sample.jpg",
        })
        self.assertEqual(response.status_code, 302)

    def test_edit_item_requires_staff(self):
        """Test that editing a menu item is restricted to staff users."""
        response = self.client.post(reverse("edit_item", args=[self.item.id]), {
            "menu_item": self.menu_item.id,
            "name": "Updated Dish",
            "description": "Updated Description",
            "price": 15.99,
            "image": "https://res.cloudinary.com/demo/image/upload/v1581091179/sample.jpg",
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_menu_requires_staff(self):
        """Test that deleting a menu is restricted to staff users."""
        response = self.client.post(reverse("delete_menu", args=[self.menu.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_menu_item_requires_staff(self):
        """Test that deleting a menu category is restricted to staff users."""
        response = self.client.post(reverse("delete_menu_item", args=[self.menu_item.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_item_requires_staff(self):
        """Test that deleting a menu item is restricted to staff users."""
        response = self.client.post(reverse("delete_item", args=[self.item.id]))
        self.assertEqual(response.status_code, 302)

    def test_set_active_menu_requires_staff(self):
        """Test that only staff can set an active menu."""
        response = self.client.post(reverse("set_active_menu", args=[self.inactive_menu.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_staff_can_set_active_menu(self):
        """Test that a staff member can set a menu as active."""
        self.client.login(email="staff@test.com", password="password123")
        response = self.client.post(reverse("set_active_menu", args=[self.inactive_menu.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to staff menu
        self.inactive_menu.refresh_from_db()
        self.assertTrue(self.inactive_menu.is_active)

    # -------------------------------------
    #  Error Handler Views Tests
    # -------------------------------------
    def test_404_error_page(self):
        """Test that the custom 404 error page is displayed."""
        response = self.client.get("/non-existent-url/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_403_error_page(self):
        """Test that the custom 403 error page is displayed."""
        response = self.client.get(reverse("no_access"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/no_access.html")

    def test_500_error_page(self):
        """Simulate a server error to test the 500 page."""
        with self.settings(DEBUG=False):
            response = self.client.get("/cause-500/")
            self.assertEqual(response.status_code, 500)
            self.assertTemplateUsed(response, "500.html")

    def test_400_error_page(self):
        """Test that the custom 400 error page is displayed."""
        response = self.client.get("/invalid-url/?param=%%%")
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, "400.html")