from django.db import models
from django.utils import timezone

# Create your models here.

class Parking(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    hourRate = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    address = models.CharField(max_length=200, default='')
    phoneNumber = models.IntegerField(default=0)

    carSlots = models.IntegerField(default=0)
    openingHours = models.CharField(max_length=200, default='')

    notes = models.CharField(max_length=400, default='')
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True)

    checkin_datetime = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    checkout_datetime = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)

    phone_number = models.CharField(max_length=20)