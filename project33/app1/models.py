from django.db import models

# Create your models here.
class eployee(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    salary = models.FloatField(blank=True,null=True)

    def __str__(self):
        return f'{self.empno} {self.ename} {self.salary}'