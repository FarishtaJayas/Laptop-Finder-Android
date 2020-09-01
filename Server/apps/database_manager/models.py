import os
from django.db import models
from .models import *

# Create your models here.


class Users(models.Model):
    user_id = models.CharField(unique=True, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_id}-{self.first_name}"

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = verbose_name

class laptop_properties(models.Model):
    lapID = models.CharField(unique=True, max_length=100)
    lapBrand = models.CharField(max_length=100)
    lapModel = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, default="")
    rating = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.lapBrand} {self.lapModel}"

    class Meta:
        verbose_name = 'Laptop Properties'
        verbose_name_plural = verbose_name



class records(models.Model):
    u_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    l_id = models.ForeignKey(
        laptop_properties, on_delete=models.CASCADE, blank=False)
    recordID = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Records'
        verbose_name_plural = verbose_name