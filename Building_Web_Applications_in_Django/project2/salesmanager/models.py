from django.db import models

# Create your models here.

class clients(models.Model):
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=50)
    email=models.EmailField()
    phone = models.CharField(max_length=7)

class items(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

class sales(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    deliver = models.BooleanField()