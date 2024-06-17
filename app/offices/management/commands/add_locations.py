from django.core.management.base import BaseCommand
from ...models import Location

class Command(BaseCommand):
    help = 'Add Castries and Vieux Fort locations to the Location model'

    def handle(self, *args, **kwargs):
        locations = ['Castries', 'Vieux Fort']
        for location_name in locations:
            location, created = Location.objects.get_or_create(location=location_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added location: {location_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Location already exists: {location_name}'))
