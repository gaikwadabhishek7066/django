from django.shortcuts import render
from app1.models import Employee
# Create your views here.
def dispay_emp(request):
    qs = Employee.objects.all()
    return render(request,'app1/display.html',context={'qs':qs})

def view_emp(request):
    j = request.GET['job']
    if j !='all':
        qs = Employee.objects.filter(job=j)
    else:
        qs = Employee.objects.all()
    
    response = render(request,"app1/show_emp.html",context={'qs':qs})
    return response

def display_empjob(request):
    return render(request,'app1/view_emp.html')