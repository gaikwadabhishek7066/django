from django import forms

class Registerform(forms.Form):
    name=forms.CharField(label="Name",max_length=20)
    user=forms.CharField(label="UserName",max_length=20)
    pwd=forms.CharField(label="Password",max_length=20)
