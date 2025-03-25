from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sub1 = models.CharField(max_length=100)
    sub2 = models.CharField(max_length=100)
