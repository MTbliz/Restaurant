from django.db import models
import datetime


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.CharField(max_length=250)
    create_time = models.DateTimeField(default=datetime.datetime.now())
