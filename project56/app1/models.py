from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    pwd = models.CharField(max_length=10)