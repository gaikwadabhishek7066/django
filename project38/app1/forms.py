from app1.models import User,Login
from django import forms

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"