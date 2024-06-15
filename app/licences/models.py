from django.db import models
from owners.models import Owner


class LicenceType(models.Model):
    licence_type = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.licence_type


class Licence(models.Model):
    licence = models.ForeignKey(LicenceType, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.owner} - {self.licence}"
