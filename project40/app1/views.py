from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Employee
# Create your views here.

def home(request):
    response = render(request, 'app1/home.html')
    return response

def create_view(request):
    dpt_id = request.GET['dpt_id']
    full_name = request.GET['full_name']
    dpt = request.GET['dpt']
    salary = request.GET['salary']
    emp = Employee(dpt_id=dpt_id,full_name=full_name,dpt=dpt,salary=salary)
    emp.save()
    response = render(request, 'app1/create.html', {'msg':'Employee created'})
    return response
    
    
def create(request):
    response = render(request, 'app1/create.html')
    return response



def emplist_view(request):
    emp = Employee.objects.all()
    response = render(request, 'app1/list.html', context={'emp':emp})
    return response

def index(request):
    response = render(request, 'app1/home.html')
    return response

def update(request):
    response = render(request, 'app1/update.html')
    return response

def update_view(request):
    dpt_id = request.GET['dpt_id']
    full_name = request.GET['full_name']
    dpt = request.GET['dpt']
    salary = request.GET['salary']
    emp = Employee.objects.get(dpt_id=dpt_id)
    try:
        emp.full_name = full_name
        emp.dpt = dpt
        emp.salary = salary
        emp.save()
        response = render(request, 'app1/update.html', context={'msg':'Employee Updated...'})
        return response
    except:
        response = render(request, 'app1/update.html', context={'msg':'Invalid Dpt id...'})
        return response


def delete_view(request):
    dpt_id = request.GET['dpt_id']
    emp = Employee.objects.get(dpt_id=dpt_id)
    emp.delete()
    response = render(request, 'app1/delete.html', context={'msg':'Employee deleted successfully'})
    return response

def delete(Request):
    return render(Request, 'app1/delete.html')