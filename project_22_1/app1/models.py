from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=15)
    fee = models.FloatField()

    def __str__(self):
        return f'{self.name}, {self.course}, {self.fee}'

