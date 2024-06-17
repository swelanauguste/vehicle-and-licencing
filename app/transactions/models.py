from django.db import models
from insurers.models import Insured
from licences.models import Licence
from offices.models import Location
from vehicles.models import Vehicle
from django.urls import reverse

class TransactionInsurance(models.Model):
    insurance = models.ForeignKey(
        Insured, blank=True, on_delete=models.SET_NULL, null=True
    )
    paid_at = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date_paid = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    receipt_number = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("transactions:insurance-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.insurance} ${self.amount} {self.receipt_number}"


class TransactionLicence(models.Model):
    licence = models.ForeignKey(
        Licence, blank=True, on_delete=models.SET_NULL, null=True
    )
    paid_at = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date_paid = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    receipt_number = models.CharField(max_length=255, unique=True)
    
    def get_absolute_url(self):
        return reverse("transactions:licence-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.licence} ${self.amount} {self.receipt_number}"


class TransactionVehicle(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, blank=True, on_delete=models.SET_NULL, null=True
    )
    paid_at = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date_paid = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    receipt_number = models.CharField(max_length=255, unique=True)
    
    def get_absolute_url(self):
        return reverse("transactions:vehicle-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.vehicle} ${self.amount} {self.receipt_number}"
