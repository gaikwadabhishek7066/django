from django.shortcuts import render
from app1.forms import StudentForm
from django.http import HttpResponse
# Create your views here.

def stud_temp(request):
    sf = StudentForm
    response = render(request, "app1/studentreg.html",context={'sf':sf})
    return response

def stud_reg(request):
    response = HttpResponse("this is student Registration")
    return response