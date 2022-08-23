from django.db import models
from authentication.models import UserModel


class DevicesType(models.Model):
    class Meta:
        verbose_name_plural = "Devices Type"
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Devices(models.Model):
    class Meta:
        verbose_name_plural = "Devices"

    company = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    price = models.FloatField(null=True)
    description = models.TextField(blank=True, null=False)
    type = models.ForeignKey(DevicesType, on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.company

    def __repr__(self):
        return f"<Device #{self.pk} {self.company!r}>"


class Slider(models.Model):
    image = models.ImageField(upload_to='images/slider')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
