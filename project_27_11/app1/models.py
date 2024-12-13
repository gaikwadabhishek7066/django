from django.db import models

# Create your models here.

class dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20)


class employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    sal = models.FloatField()
    dept = models.ForeignKey(dept, on_delete=models.CASCADE)