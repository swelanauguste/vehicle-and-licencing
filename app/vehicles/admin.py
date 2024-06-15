from django.contrib import admin

from .models import Manufacturer, ModelYear, Vehicle, VehicleModel

admin.site.register(Manufacturer)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)
admin.site.register(ModelYear)
