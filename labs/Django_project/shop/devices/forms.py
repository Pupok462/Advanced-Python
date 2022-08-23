from django.forms import ModelForm
from .models import Devices


class DeviceCreateForm(ModelForm):

    class Meta:
        model = Devices
        fields = "company", "model", "price", "description", "type", "image"



