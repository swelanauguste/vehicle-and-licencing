from django.db import models
from django.shortcuts import reverse
from owners.models import Owner


class LicenceType(models.Model):
    licence_type = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("licences:detail-type", kwargs={"pk": self.pk})

    def __str__(self):
        return self.licence_type


class Licence(models.Model):
    licence = models.ForeignKey(LicenceType, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse("licences:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.owner} - {self.licence}"
