from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    sal = models.FloatField()
    

    class Meta:
        managed = False
        db_table = 'app1_employee'