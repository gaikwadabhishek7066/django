from django.shortcuts import render
import datetime
# Create your views here.

def show_employee_data(request):
    emp_data={101:['naresh',5000],
              102:['suresh',6000],
              103:['',9000],
              104:['ramesh',0]}
    response=render(request,'app1/show_emp.html',{'emp_data':emp_data})
    return response
