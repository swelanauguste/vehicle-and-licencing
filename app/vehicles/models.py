from django.db import models
from django.urls import reverse
from owners.models import Owner


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.manufacturer


class ModelYear(models.Model):
    year = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"{self.year}"


class VehicleModel(models.Model):
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.model


class VehicleColour(models.Model):
    colour = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.colour


class Vehicle(models.Model):
    owners = models.ManyToManyField(Owner)
    licence_number = models.CharField(max_length=8)
    reg_on = models.DateField(blank=True, null=True, verbose_name="registered on")
    number = models.PositiveIntegerField()
    previous_owner = models.BooleanField(default=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(ModelYear, on_delete=models.SET_NULL, null=True)
    tare_weight = models.PositiveIntegerField()
    chassis_number = models.CharField(max_length=255, unique=True)
    engine_number = models.CharField(max_length=255)
    engine_capacity = models.CharField(max_length=255, verbose_name="cc")

    def get_absolute_url(self):
        return reverse("vehicles:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}"
