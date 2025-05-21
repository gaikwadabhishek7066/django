from django.db import models

# Create your models here.
class Product(models.Model):
    prodid = models.IntegerField(primary_key=True)
    prodname = models.CharField(max_length=100)
    price = models.FloatField()