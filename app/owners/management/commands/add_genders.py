from django.core.management.base import BaseCommand
from ...models import Gender

class Command(BaseCommand):
    help = 'Add Male and Female genders to the Gender model'

    def handle(self, *args, **kwargs):
        genders = ['male', 'female']
        for gender_name in genders:
            gender, created = Gender.objects.get_or_create(gender=gender_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added gender: {gender_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Gender already exists: {gender_name}'))
