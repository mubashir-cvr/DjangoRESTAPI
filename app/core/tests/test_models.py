from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test Creating a new user with email"""
        email = "emaple@mail.com"
        password = "mb@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user_with_email_successfull(self):
        """Test Creating a new user with email"""
        email = "emaple@mail.com"
        password = "mb@123"
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
