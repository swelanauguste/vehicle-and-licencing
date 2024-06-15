from django.contrib import admin

from .models import Insured, Insurer

admin.site.register(Insurer)
admin.site.register(Insured)
