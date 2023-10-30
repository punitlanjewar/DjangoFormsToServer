from django.db import models

# Create your models here.
class CarData1(models.Model):
    c_name = models.CharField(max_length=150)
    c_company = models.CharField(max_length=150)
    c_model = models.CharField(max_length=150)
    c_price = models.BigIntegerField()
    c_fueltype = models.CharField(max_length=150)