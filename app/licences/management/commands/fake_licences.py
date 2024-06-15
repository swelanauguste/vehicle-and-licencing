import random
from django.core.management.base import BaseCommand
from owners.models import Owner
from ...models import LicenceType, Licence

class Command(BaseCommand):
    help = 'Populate the database with vehicle licence types and assign licences to owners'

    def handle(self, *args, **kwargs):
        # Define vehicle licence types and descriptions
        licence_types = [
            {'licence_type': 'Class A', 'description': 'Motorcycles'},
            {'licence_type': 'Class B', 'description': 'Passenger vehicles up to 8 seats'},
            {'licence_type': 'Class C', 'description': 'Light trucks and vans'},
            {'licence_type': 'Class D', 'description': 'Heavy trucks'},
            {'licence_type': 'Class E', 'description': 'Combination vehicles'},
            {'licence_type': 'Class F', 'description': 'Farm equipment'},
            {'licence_type': 'Class G', 'description': 'General vehicle operator'},
            {'licence_type': 'Class H', 'description': 'Hazardous materials'},
            {'licence_type': 'Class I', 'description': 'Motorcycles with sidecars'},
            {'licence_type': 'Class J', 'description': 'School bus driver'},
        ]

        # Populate LicenceType
        for licence_data in licence_types:
            LicenceType.objects.get_or_create(
                licence_type=licence_data['licence_type'],
                defaults={'description': licence_data['description']}
            )

        licence_types = list(LicenceType.objects.all())
        owners = list(Owner.objects.all())

        licences = []

        for owner in owners:
            licence_type = random.choice(licence_types)
            licences.append(Licence(
                licence=licence_type,
                owner=owner
            ))

        Licence.objects.bulk_create(licences)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated licence types and assigned licences to owners'))
