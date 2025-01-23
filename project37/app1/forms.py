from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=20)
    user = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)