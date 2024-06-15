from django.contrib import admin

from .models import Owner, Gender

admin.site.register(Gender)
admin.site.register(Owner)
