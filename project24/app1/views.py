from django.shortcuts import render
import datetime
# Create your views here.

def show_employee_data(request):
    emp_data ={101:['thokal', datetime.date(2003,6,12)],
               102:['Abhi', datetime.date(2002,11,9)],
               103:['yogesh', datetime.date(2003,6,13)]
               }
    response = render(request, 'app1/show_emp.html', context={'emp_data':emp_data})
    return response
    
