from django.shortcuts import render
from app1.forms import Registerform

# Create your views here.

def register_temp(request):
    f1 = Registerform()
    response = render(request, "app1/register.html", context={'f1': f1})
    return response
