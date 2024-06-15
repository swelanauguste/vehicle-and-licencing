from django.db import models
from inspectors.models import Inspector
from offices.models import Location
from owners.models import Owner
from vehicles.models import Vehicle


class Insurer(models.Model):
    insurer = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.insurer


class Insured(models.Model):
    insurer = models.ForeignKey(Insurer, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    inspected_by = models.ForeignKey(Inspector, on_delete=models.SET_NULL, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    date_insured = models.DateField(blank=True, null=True)
    expires = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'insured'

    def __str__(self):
        return f"{self.insurer} {self.vehicle} {self.expires}"
