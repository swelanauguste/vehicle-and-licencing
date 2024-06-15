from django.db import models
from offices.models import Location
from owners.models import Owner
from vehicles.models import Vehicle
from inspectors.models import Inspector


class Insurer(models.Model):
    insurer = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.insurer


class Insured(models.Model):
    insurer = models.ForeignKey(Insurer, on_delete=models.SET_NULL, null=True)
    owner = models.ManyToManyField(Owner)
    vehicle = models.ForeignKey(Vehicle)
    inspected_by = models.ForeignKey(Inspector)
    inspection_date = models.DateField(blank=True, null=True)
    paid_at = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    expires = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.insurer} {self.owner} {self.vehicle} {self.expires}"
