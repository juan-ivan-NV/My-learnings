from django.db import models

# Create your models here.


class clients(models.Model):
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=50, verbose_name='address') # To change direction to address
    email = models.EmailField(blank=True, null=True)  # to admit nulls
    phone = models.CharField(max_length=7)  # max 7 numbers
    
    def __str__(self):
        return self.name


class items(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return 'Name %s section %s price %s' % (self.name, self.section, self.price)


class sales(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    deliver = models.BooleanField()
