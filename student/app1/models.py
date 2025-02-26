from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    