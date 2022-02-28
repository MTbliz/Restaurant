from django.db import models
import datetime


# Create your models here.
class User(models.Model):
    user = models.TextField(default=None)
    visit_time = models.DateTimeField(default=None)


