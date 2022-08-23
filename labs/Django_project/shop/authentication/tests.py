from authentication.forms import UserCreationForm, UserLoginForm
from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from authentication.models import UserModel


class UserLoginTestCase(TestCase):

    def setUp(self) -> None:
        password = "user_john"
        self.user: AbstractUser = UserModel.objects.create_user(
            "user_john",
            "user_john@example.com",
            password,
        )
        self.password = password

    def test_user_login(self):
        response = self.client.post(
            reverse("login"),
            data={
                "username": self.user.username,
                "password": self.password,
            },
        )

        self.assertEqual(response.url, reverse("devices:devices-list"))

        response = self.client.get(reverse("devices:devices-list"))
        self.assertFalse(response.context["user"].is_anonymous)


class UserRegisterTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_reg_data = {
            "username": "user_john",
            "email": "user_john@example.com",
            "password1": "qazwsxuserjohn",
            "password2": "qazwsxuserjohn",
        }

        cls.user_reg_data_invalid_pass = {
            "username": "user_john",
            "email": "user_john@example.com",
            "password1": "qazwsx_user_john",
            "password2": "qazwsx_user_sam",
        }

        cls.user_reg_data_not_unique_username = {
            "username": "sam",
            "email": "user_sam@example.com",
            "password1": "samsamsam",
            "password2": "samsamsam",
        }

    def test_user_register_username_exists_error(self):
        response = self.client.post(
            reverse("register"),
            data=self.user_reg_data_not_unique_username,
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            reverse("register"),
            data=self.user_reg_data_not_unique_username,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "username",
            _("A user with that username already exists."),
        )

    def test_user_register_password_doesnt_match(self):
        response = self.client.post(
            reverse("register"),
            data=self.user_reg_data_invalid_pass,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "password2",
            UserCreationForm.error_messages["password_mismatch"],
        )

    def test_user_register_success(self):
        response = self.client.post(
            reverse("register"),
            data=self.user_reg_data,
        )
        self.assertEqual(response.status_code, 302)

        user: AbstractUser = UserModel.objects.get(username=self.user_reg_data["username"])
        self.assertEqual(user.email, self.user_reg_data["email"])

