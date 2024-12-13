from django.forms import ModelForm
from app1.models import Employee

class EmployeeForm(ModelForm):
    class meta:
        model=Employee
        fields='__all__'