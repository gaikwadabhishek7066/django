from django.shortcuts import render
import datetime
# Create your views here.

def show_emp(request):
    emp_data = {
        101:['abhi',datetime.date(2002,9,11)],
        102:['yogesh',datetime.date(2003,6,13)],
        103:['ajinkya',datetime.date(2007,3,10)]
    }
    return render(request, 'app1/emp.html', context={'emp_data':emp_data})