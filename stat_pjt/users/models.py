from django.db import models
from clubs.models import club

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    balance = models.IntegerField()
    image = models.ImageField(blank=True)
    clubs = models.ManyToManyField(club, related_name = 'users')

