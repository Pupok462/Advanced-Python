from django.test import TestCase
from django.urls import reverse
from devices.models import Devices


class DevicesTestCase(TestCase):
    fixtures = ["devices.fixture.json", "devices_type.fixture.json"]

    def devices_quantity(self):
        response = self.client.get(
            reverse("devices:tests-list")
        )
        self.assertEqual(response.status_code, 200)

        devices_list = Devices.objects.all()
        devices_list_in_context = response.context["devices"]

        self.assertEqual(devices_list, devices_list_in_context)