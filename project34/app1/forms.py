from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Student Name",max_length=20)
    c1 =forms.BooleanField(label="python",required=False)
    c2 = forms.BooleanField(label="java",required=False)
    c3 = forms.BooleanField(label="c++",required=False)
    