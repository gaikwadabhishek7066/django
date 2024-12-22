from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)

class Mails(models.Model):
    user_from = models.CharField(max_length=20)
    user_to = models.ForeignKey(Users,on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
   
