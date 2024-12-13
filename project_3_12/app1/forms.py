from django import forms

class StudentForm(forms.Form):
    rollno = forms.IntegerField(label="Student rollno")
    name = forms.CharField(label="Student name", max_length=20)
    coures = forms.CharField(label="Student coures", max_length=20)
    fee = forms.FloatField(label="Student fee")