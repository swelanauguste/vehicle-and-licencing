from django.contrib import admin

from .models import (
    TransactionInsurance,
    TransactionLicence,
    TransactionVehicle,
)

admin.site.register(TransactionLicence)
admin.site.register(TransactionInsurance)
admin.site.register(TransactionVehicle)
