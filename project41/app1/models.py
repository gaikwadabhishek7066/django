from django.db import models

# Create your models here.
class User(models.Model):
 
    username = models.CharField(max_length=20,unique=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
     
