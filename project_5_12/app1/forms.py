from django import forms
from django.core.exceptions import ValidationError
'''
class UserForm(forms.Form):
    name = forms.CharField(validators="name")
    username = forms.CharField(validators="username")
    password = forms.CharField(validators="password", widget=forms.PasswordInput())
    repassword = forms.CharField(validators="repassword", widget=forms.PasswordInput())
    email = forms.EmailField(validators="email")
'''
class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True, min_length=8)
    repassword = forms.CharField( widget=forms.PasswordInput(),required=True)
    email = forms.EmailField(required=True)

    # Form-level validation for passwords
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")

        if password and repassword and password != repassword:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        min_length=8
    )
    repassword = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )
    email = forms.EmailField(required=True)

    # Form-level validation for passwords
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")

        if password and repassword and password != repassword:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        min_length=8
    )
    repassword = forms.CharField(widget=forms.PasswordInput(),
        required=True
    )
    email = forms.EmailField(required=True)

    # Form-level validation for passwords
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")

        if password and repassword and password != repassword:
            raise ValidationError("Passwords do not match.")

        return cleaned_data