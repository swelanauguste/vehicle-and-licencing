from django.db import models
from offices.models import Location


class Sex(models.Model):
    sex = models.CharField(max_length=255)

    def __str__(self):
        return self.sex


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nis = models.CharField(max_length=10, unique=True)
    driver_number = models.CharField(max_length=255)
    driver_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    location_code = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, null=True)
    date_of_medical = models.DateField(blank=True, verbose_name="date of medical exam")
    reg_date = models.DateField(blank=True, null=True, verbose_name="registration date")

    def __str__(self):
        return f"{self.frist_name} {self.last_name} {self.driver_number}"
