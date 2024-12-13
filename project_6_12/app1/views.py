from django.shortcuts import render
from app1.forms import EmployeeForm

# Create your views here.
def addemp_view(request):
  if request.method == 'GET':
   emp_form = EmployeeForm()
   response = render(request, 'app1/addemp_temp.html', context={'emp_form': emp_form})
   return response
  elif request.method == 'POST':
   emp_form = EmployeeForm(request.POST)
   if emp_form.is_valid():
    emp_form.save(commit=True)
    emp_form=EmployeeForm()
    response = render(request, 'aap1/addemp_temp.html', {'emp_form': emp_form, 'msg':"Employee Added..."})
    return response
   else:
    response = render(request, 'app1/addemp_temp.html', context={'emp_form': emp_form})
    return response
