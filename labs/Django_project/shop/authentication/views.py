from .forms import UserCreationForm, UserLoginForm
from .models import UserProfile, UserModel
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as LoginClass
from django.contrib.auth.views import LogoutView as LogoutClass


class UserProfileView(DetailView):
    queryset = UserProfile.objects.select_related('user')
    context_object_name = "profile"
    template_name = "registration/profile.html"


class UserCreationView(CreateView):
    model = UserModel
    success_url = reverse_lazy("devices:devices-list")
    form_class = UserCreationForm
    template_name = "registration/create.html"


class LoginView(LoginClass):
    next_page = reverse_lazy("devices:devices-list")
    form_class = UserLoginForm


class LogoutView(LogoutClass):
    next_page = reverse_lazy("devices:devices-list")



