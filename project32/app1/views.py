from django.shortcuts import render
from app1.models import *

# Create your views here.
def home(request):
    response = render(request, 'app1/index.html')
    return response

def addept_temp(request):
     response = render(request, 'app1/addept.html')
     return response 
def addemp_temp(request):
     qs = Dept.objects.all()
     dept = []
     for row in qs:
          dept.append(row.deptno)
     response = render(request, 'app1/addemp.html', {'dept':dept})
     return response

def listemp_temp(request):
     dept=request.all()
     dept = []
     for row in dept:
          dept.append(row.deptno)
     response = render(request, 'app1/listemp.html', {'Dept': dept})
     return response

def create_dept(request):
     deptno = int(request.GET['deptno'])
     deptname = request.GET['dname']
     try:
        d=Dept.objects.create(deptno=deptno,dname=deptname)
        d.save()
        msg = 'Department Added'
     except:
        msg = 'Invalid Deptno'

     response = render(request, 'app1/addemp.html',context={'msg':msg})
     return response

def create_emp(request):
    empno=int(request.GET['empno'])
    ename=request.GET['ename']
    job=request.GET['job']
    sal=float(request.GET['sal'])
    deptno=int(request.GET['deptno'])
    try:
        dept=Dept.objects.get(deptno=deptno)
        e=Employee.objects.create(empno=empno,ename=ename,job=job,sal=sal,dept=dept)
        e.save()
        msg="Employee Added"
    except:
        msg="Error in Adding Employee"


    response=render(request,"app1/addemp.html",context={'msg':msg})
    return response 

def disp_emp(request):
    deptno=int(request.GET['deptno'])
    dept=Dept.objects.get(deptno=deptno)
    qs=Employee.objects.filter(dept=dept)
    response = render(request, 'app1/listemp.html',context={'qs':qs})
    return response
