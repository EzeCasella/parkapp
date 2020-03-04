from django.db import models

# Create your models here.

class Parking(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    hourRate = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    

    def __str__(self):
        return self.name

