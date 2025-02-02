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