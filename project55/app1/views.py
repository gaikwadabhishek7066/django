from django.shortcuts import render
from .models import Employee
# Create your views here.
def index(request):
    return render(request, 'app1/home.html')

def add_emp(request):
    emp_id = request.GET['emp_id']
    name = request.GET['name']
    salary = request.GET['salary']
    emp = Employee(emp_id=emp_id, name=name,salary=salary)
    emp.save()
    return render(request, 'app1/add.html', context={'msg':"Employee added..."})

def add_view(request):
    return render(request, 'app1/add.html')

def list_view(request):
    emp = Employee.objects.all()
    return render(request, 'app1/list.html', context={'emp':emp})

def update_temp(request):
    return render(request, 'app1/update.html')

def update_view(request):
    emp_id = request.GET['emp_id']
    salary = request.GET['salary']
    try:
        e = Employee.objects.get(emp_id=emp_id)
        e.salary = salary
        e.save()
        return render(request, 'app1/update.html', context={'msg':"Update successfully..."})
    except:
        return render(request, 'app1/update.html', context={'msg':'Invalid Employee ID...'})
    

def delete_temp(request):
    return render(request, 'app1/delete.html')

def delete_view(request):
     emp_id = request.GET['emp_id']
     e = Employee(emp_id=emp_id)
     e.delete()
     return render(request, 'app1/delete.html',context={'msg':"Delete Employee data..."})