from django.shortcuts import render
from app1.models import Emp
# Create your views here.
def add_view(request):
    empno = request.GET['empno']
    name = request.GET['name']
    job = request.GET['job']
    sal = request.GET['sal']
    emp = Emp(empno=empno, name=name, job=job, sal=sal)
    emp.save()
    response = render(request, 'app1/emp.html', context={'msg':"employee added successfully"})
    return response
def home(request):
    response = render(request, 'app1/emp.html')
    return response

def update_view(request):
    empno = int(request.GET['empno'])
    update = float(request.GET['update'])
    try:
        e=Emp.objects.get(empno=empno)
        e.sal=e.sal+update
        e.save()
        response = render(request, 'app1/update.html', context={'msg':"salary updated..."})
        return response
    except:
        response = render(request, 'app1/update.html', context={'msg': "Invalid employeeno"})
        return response
def update(request):
    response=render(request, 'app1/update.html')
    return response