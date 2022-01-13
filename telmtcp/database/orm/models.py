from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class geolocation(models.Model):
    username = models.CharField(max_length=256, blank=False, null=False)
    latitude = models.CharField(max_length=16, blank=False, null=False)
    longitude = models.CharField(max_length=16, blank=False, null=False)
    accuracy = models.CharField(max_length=64, blank=False, null=False)
    location = models.CharField(max_length=64, blank=False, null=False)
    approveed = models.IntegerField(default=0)