from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Employee


# Create your views here.

def home(request):
    return HttpResponse(request, 'app1/home.html')

def emp_create(request):
    full_name = request.GET['full_name']
    emp_code = request.GET['emp_code']
    mobile = request.GET['mobile']
    Position = request.GET['position']
    emp = Employee.objects.all(full_name=full_name,emp_code=emp_code, mobile=mobile, position=Position)
    emp.save()
    response = render(request, 'app1/empcreate.html')
    return response
