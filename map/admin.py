from django.contrib import admin

# Register your models here.

from .models import Parking, Schedule

admin.site.register(Parking)
admin.site.register(Schedule)