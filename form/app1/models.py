from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    number = models.IntegerField(max_length=20)