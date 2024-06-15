from faker import Faker
from django.core.management.base import BaseCommand
from ...models import Inspector

class Command(BaseCommand):
    help = 'Populate the database with 10 fake vehicle inspector businesses'

    def handle(self, *args, **kwargs):
        fake = Faker()

        inspectors = []
        for _ in range(10):
            inspector_name = fake.company() + " Vehicle Inspections"
            inspectors.append(Inspector(inspector=inspector_name))

        Inspector.objects.bulk_create(inspectors)

        self.stdout.write(self.style.SUCCESS('Successfully added 10 fake vehicle inspector businesses'))
