from django.shortcuts import render
from app1.models import Emp
# Create your views here.

def display_emp(request):
    qs = Emp.objects.all()
    response = render(request, 'app1/display.html', context={'qs':qs})
    return response

def view_emp(request):
    j = request.GET['job']
    if j!='all':
        qs = Emp.objects.filter(job=j)
    else:
        qs = Emp.objects.all()

    response = render(request, 'app1/show_emp.html', context={'qs':qs})
    return response

def display_empjob(requset):
    response = render(requset, 'app1/view_emp.html')
    return response