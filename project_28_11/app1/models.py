from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    marks = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'student'

def __str__(self):
    return f'{self.rollno} {self.name} {self.marks}'