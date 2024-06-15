from django.contrib import admin

from .models import Licence, LicenceType

admin.site.register(Licence)
admin.site.register(LicenceType)
