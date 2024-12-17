from django.shortcuts import render
import datetime
# Create your views here.

def show_employee_data(request):
    emp_data={101:['naresh',datetime.date(2020,8,12)],
              102:['suresh',datetime.date(2020,9,10)],
              103:['ramesh',datetime.date(2020,10,11)],
              104:['suresh',datetime.date(2022,10,14)]
              }
    response=render(request,'app1/show_emp.html',{'emp_data':emp_data})
    return response
