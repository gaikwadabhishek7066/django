from django.db import models

# Create your models here.

class Employee(models.Model):
    dpt_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=20)
    dpt = models.CharField(max_length=10)
    salary = models.CharField(max_length=20)