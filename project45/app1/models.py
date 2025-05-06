from django.db import models

# Create your models here.
class it(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    course = models.CharField(max_length=100)
    fees = models.FloatField(max_length=2)
    
