from django.contrib.auth.forms import UserCreationForm as CreationForm
from django.contrib.auth.forms import ValidationError
from .models import UserModel, UserProfile
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(CreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2")


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ("username", "password")

