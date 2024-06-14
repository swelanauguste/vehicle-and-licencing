from django.db import models
from offices.models import Location

class Insurer(models.Model):
    insurer = models.CharField(max_length=255, unique=True)


class Insured(models.Model):
    insurer = models.ForeignKey(Insurer, on_delete=models.SET_NULL, null=True)
    paid_at = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    insurance_expires = models.DateField(blank=True, null=True)