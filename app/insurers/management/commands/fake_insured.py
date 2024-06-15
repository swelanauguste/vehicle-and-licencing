import random

from django.core.management.base import BaseCommand
from faker import Faker
from inspectors.models import Inspector

from ...models import Insured, Insurer, Vehicle


class Command(BaseCommand):
    help = "Populate the database with 20 fake insurers and insure 95% of vehicles"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Populate insurers
        insurers = []
        for _ in range(20):
            insurer_name = fake.company() + " Insurance"
            insurers.append(Insurer(insurer=insurer_name))

        Insurer.objects.bulk_create(insurers)
        insurers = list(Insurer.objects.all())

        # Populate insured vehicles
        vehicles = list(Vehicle.objects.all())
        inspectors = list(Inspector.objects.all())

        insured_records = []
        num_to_insure = int(len(vehicles) * 0.95)

        for vehicle in random.sample(vehicles, num_to_insure):
            insured_records.append(
                Insured(
                    insurer=random.choice(insurers),
                    vehicle=vehicle,
                    inspected_by=random.choice(inspectors),
                    inspection_date=fake.date_this_decade(),
                    date_insured=fake.date_this_decade(),
                    expires=fake.date_between(start_date="+1y", end_date="+2y"),
                )
            )

        Insured.objects.bulk_create(insured_records)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added 20 fake insurers and insured {num_to_insure} vehicles"
            )
        )
