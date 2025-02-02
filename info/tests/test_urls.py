from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUrls(TestCase):
    """Unit Tests for info app urls"""

    def setUp(self):
        username = "testuser"
        email = "testapp@test.com"
        password = "12339292sss4"
        user_model = get_user_model()
        self.user = user_model.objects.create_superuser(
            email=email,
            password=password,
            username=username
        )
        login = self.client.login(email=email, password=password)
        self.assertTrue(login)
        self.assertTrue(self.user.is_superuser)

    def test_home_page(self):
        """Testing the homepage url"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """Testing the about page url"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_menu_page(self):
        """Testing the menu page url"""
        response = self.client.get("/menu/")
        self.assertEqual(response.status_code, 200)

    def test_set_sail_page(self):
        """Testing the set sail page url"""
        response = self.client.get("/set-sail/")
        self.assertEqual(response.status_code, 200)

    def test_staff_menu_page(self):
        """Testing the staff menu page url"""
        response = self.client.get("/staff/menu/")
        self.assertEqual(response.status_code, 200)

    def test_staff_menu_page_logout(self):
        """Testing the staff menu logout url"""
        self.client.logout()
        response = self.client.get("/staff/menu/")
        self.assertEqual(response.status_code, 302)

    def test_add_menu_page(self):
        """Testing the add menu page url"""
        response = self.client.get("/staff/menu/add/")
        self.assertEqual(response.status_code, 200)

    def test_edit_menu_page(self):
        """Testing the edit menu page url with a dummy ID"""
        response = self.client.get("/staff/menu/edit/1/")
        self.assertEqual(response.status_code, 404)

    def test_delete_menu_page(self):
        """Testing the delete menu page url with a dummy ID"""
        response = self.client.get("/staff/menu/delete/1/")
        self.assertEqual(response.status_code, 404)

    def test_set_active_menu_page(self):
        """Testing the set active menu page url with a dummy ID"""
        response = self.client.get("/staff/menu/set-active/1/")
        self.assertEqual(response.status_code, 404)

    def test_add_menu_item_page(self):
        """Testing the add menu item page url"""
        response = self.client.get("/staff/menu-item/add/")
        self.assertEqual(response.status_code, 200)

    def test_edit_menu_item_page(self):
        """Testing the edit menu item page url with a dummy ID"""
        response = self.client.get("/staff/menu-item/edit/1/")
        self.assertEqual(response.status_code, 404)

    def test_delete_menu_item_page(self):
        """Testing the delete menu item page url with a dummy ID"""
        response = self.client.get("/staff/menu-item/delete/1/")
        self.assertEqual(response.status_code, 404)

    def test_add_item_page(self):
        """Testing the add item page url"""
        response = self.client.get("/staff/item/add/")
        self.assertEqual(response.status_code, 200)

    def test_edit_item_page(self):
        """Testing the edit item page url with a dummy ID"""
        response = self.client.get("/staff/item/edit/1/")
        self.assertEqual(response.status_code, 404)

    def test_delete_item_page(self):
        """Testing the delete item page url with a dummy ID"""
        response = self.client.get("/staff/item/delete/1/")
        self.assertEqual(response.status_code, 404)

    def test_no_access_page(self):
        """Testing the no access page url"""
        response = self.client.get("/no-access/")
        self.assertEqual(response.status_code, 200)