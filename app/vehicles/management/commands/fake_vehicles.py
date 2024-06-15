import random

from django.core.management.base import BaseCommand
from faker import Faker
from owners.models import Owner

from ...models import Manufacturer, ModelYear, Vehicle, VehicleColour, VehicleModel


class Command(BaseCommand):
    help = "Populate the database with real-world manufacturers, models, colours, and fake vehicles"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Real-world data
        manufacturers = ["Toyota", "Ford", "Chevrolet", "Honda", "Nissan"]
        models = {
            "Toyota": ["Camry", "Corolla", "Prius"],
            "Ford": ["Focus", "Fiesta", "Mustang"],
            "Chevrolet": ["Malibu", "Impala", "Camaro"],
            "Honda": ["Civic", "Accord", "Fit"],
            "Nissan": ["Altima", "Sentra", "Maxima"],
        }
        colours = ["Red", "Blue", "Black", "White", "Gray", "Silver"]
        years = list(range(1988, 2024))

        # Populate manufacturers
        for manufacturer_name in manufacturers:
            Manufacturer.objects.get_or_create(manufacturer=manufacturer_name)

        # Populate vehicle models
        for manufacturer_name, model_list in models.items():
            manufacturer = Manufacturer.objects.get(manufacturer=manufacturer_name)
            for model_name in model_list:
                VehicleModel.objects.get_or_create(model=model_name)

        # Populate colours
        for colour_name in colours:
            VehicleColour.objects.get_or_create(colour=colour_name)

        # Populate model years
        for year in years:
            ModelYear.objects.get_or_create(year=year)

        # Create vehicles and link to owners
        owners = list(Owner.objects.all())
        manufacturers = list(Manufacturer.objects.all())
        vehicle_models = list(VehicleModel.objects.all())
        vehicle_colours = list(VehicleColour.objects.all())
        model_years = list(ModelYear.objects.all())

        vehicles = []

        for _ in range(10000):
            vehicle = Vehicle(
                licence_number=fake.unique.license_plate(),
                reg_on=fake.date_this_decade(),
                number=fake.random_int(min=1, max=1000000),
                previous_owner=fake.boolean(),
                manufacturer=random.choice(manufacturers),
                model=random.choice(vehicle_models),
                year=random.choice(model_years),
                tare_weight=fake.random_int(min=1000, max=5000),
                chassis_number=fake.unique.numerify(text="CH#######"),
                engine_number=fake.unique.numerify(text="EN#######"),
                engine_capacity=fake.random_int(min=1000, max=5000),
            )
            vehicle.save()
            vehicle.owners.set(random.sample(owners, k=random.randint(1, 3)))
            vehicles.append(vehicle)

        Vehicle.objects.bulk_create(vehicles, batch_size=1000)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully added real-world data and 10,000 fake vehicles"
            )
        )
