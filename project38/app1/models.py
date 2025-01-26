from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    
class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)