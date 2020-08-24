from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = "deshan5255@gmail.com"
        password = 'test1234'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = "deshan5255@GMAIL.COM"
        password = 'test1234'

        user = get_user_model().objects.create_user(email, password)

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'deshan5255@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
