from django.shortcuts import render
from app1.models import *

# Create your views here.

def home(request):
    response = render(request, "app1/index.html")
    return response

def adddept_temp(request):
    response = render(request, "app1/adddept.html")
    return response

def addemp_temp(request):
    qs = dept.objects.all()
    Dept = []
    for row in qs:
        Dept.append(row.deptno)
    response = render(request, "app1/addemp.html", context={'Dept':Dept})
    return response

def listemp_temp(request):
    qs = dept.objects.all()
    Dept = []
    for row in qs:
        Dept.append(row.deptno)
    response = render(request, "app1/listemp.html", context={'Dept':Dept})
    return response

def create_dept(request):
    deptno=int(request.GET['deptno'])
    deptname=request.GET['dname']
    try:
        d=dept.objects.create(deptno=deptno,dname=deptname)
        d.save()
        msg="Department Added..."
    except:
        msg="Invalid Deptno"
    response=render(request,"app1/adddept.html",context={'msg':msg})
    return response
def create_emp(request):
    empno=int(request.GET['empno'])
    ename=request.GET['ename']
    job=request.GET['job']
    sal=float(request.GET['sal'])
    deptno=int(request.GET['deptno'])
    try:
        Dept=dept.objects.get(deptno=deptno)
        e=employee.objects.create(empno=empno,ename=ename,job=job,sal=sal,dept=Dept)
        e.save()
        msg="Employee Added"
    except:
        msg="Error in Adding Employee"


    response=render(request,"app1/addemp.html",context={'msg':msg})
    return response 
def disp_emp(request):
    deptno=int(request.GET['deptno'])
    dept=dept.objects.get(deptno=deptno)
    qs=employee.objects.filter(dept=dept)
    response=render(request,"app1/listemp.html",context={'qs':qs})
    return response

def addemp_temp(request):
    response=render(request,"app1/addemp.html")
    return response

