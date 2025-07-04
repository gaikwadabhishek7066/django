from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=20)

class Mail(models.Model):
    from_user = models.CharField(max_length=20)
    to_user = models.ForeignKey(Users,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)