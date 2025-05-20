from django.shortcuts import render
import datetime
# Create your views here.
def show_employee_data(request):
    emp_data=[{'empno':101, 'ename':'naresh', 'sal':20000},
              {'empno':102, 'ename':'suresh', 'sal':25000},
              {'empno':103, 'ename':'ramesh', 'sal':35000},
              {'empno':104, 'ename':'kishor', 'sal':40000}
              ]
    response = render(request, 'app1/emp_data.html', context={'emp_data':emp_data})
    return response