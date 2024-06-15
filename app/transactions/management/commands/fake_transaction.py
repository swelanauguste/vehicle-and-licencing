import random

from django.core.management.base import BaseCommand
from faker import Faker
from insurers.models import Insured
from licences.models import Licence
from offices.models import Location
from transactions.models import (
    TransactionInsurance,
    TransactionLicence,
    TransactionVehicle,
)
from vehicles.models import Vehicle


class Command(BaseCommand):
    help = "Populate the database with 50 payment transactions for insurance, licences, and vehicles"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Fetch all instances of related models
        locations = list(Location.objects.all())
        insureds = list(Insured.objects.all())
        licences = list(Licence.objects.all())
        vehicles = list(Vehicle.objects.all())

        # Lists to hold the transaction instances
        transaction_insurances = []
        transaction_licences = []
        transaction_vehicles = []

        # Generate 50 transactions for each model
        for _ in range(50):
            if locations and insureds:
                transaction_insurances.append(
                    TransactionInsurance(
                        insurance=random.choice(insureds),
                        paid_at=random.choice(locations),
                        date_paid=fake.date_this_decade(),
                        amount=round(random.uniform(50.0, 500.0), 2),
                        receipt_number=fake.unique.numerify(text="INS#######"),
                    )
                )

            if locations and licences:
                transaction_licences.append(
                    TransactionLicence(
                        licence=random.choice(licences),
                        paid_at=random.choice(locations),
                        date_paid=fake.date_this_decade(),
                        amount=round(random.uniform(50.0, 500.0), 2),
                        receipt_number=fake.unique.numerify(text="LIC#######"),
                    )
                )

            if locations and vehicles:
                transaction_vehicles.append(
                    TransactionVehicle(
                        vehicle=random.choice(vehicles),
                        paid_at=random.choice(locations),
                        date_paid=fake.date_this_decade(),
                        amount=round(random.uniform(50.0, 500.0), 2),
                        receipt_number=fake.unique.numerify(text="VEH#######"),
                    )
                )

        # Bulk create transactions
        if transaction_insurances:
            TransactionInsurance.objects.bulk_create(transaction_insurances)
        if transaction_licences:
            TransactionLicence.objects.bulk_create(transaction_licences)
        if transaction_vehicles:
            TransactionVehicle.objects.bulk_create(transaction_vehicles)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added 50 payment transactions for insurance, licences, and vehicles"
            )
        )
