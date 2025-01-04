from django import forms


class StudentForm(forms.Form):
    rollno = forms.CharField(label="student rollno", max_length=10)
    name = forms.CharField(label="student name", max_length=50)
    course = forms.CharField(label="student course", max_length=50)
    fee = forms.FloatField(label="student fee")