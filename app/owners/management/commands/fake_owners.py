import random
from faker import Faker
from django.core.management.base import BaseCommand
from ...models import Owner, Gender

class Command(BaseCommand):
    help = 'Populate the database with 10,000 fake owners'

    def handle(self, *args, **kwargs):
        fake = Faker()
        genders = list(Gender.objects.all())
        owners = []

        for _ in range(10000):
            owner = Owner(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                nis=fake.unique.numerify(text='##########'),
                driver_number=fake.unique.numerify(text='##########'),
                driver_code=fake.unique.numerify(text='##########'),
                address=fake.address(),
                location_code=fake.numerify(text='##########'),
                place_of_birth=fake.city(),
                nationality=fake.country(),
                date_of_birth=fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90),
                gender=random.choice(genders) if genders else None,
                date_of_medical=fake.date_this_decade(),
                reg_date=fake.date_this_year()
            )
            owners.append(owner)

        Owner.objects.bulk_create(owners, batch_size=1000)

        self.stdout.write(self.style.SUCCESS('Successfully added 10,000 fake owners'))
