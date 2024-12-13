from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from app1.models import Employee
# Create your views here.

class AddView(View):
    def get(self,request,*vargs,**kwargs):
        num1 = int(request.GET['n1'])
        num2 = int(request.GET['n2'])
        num3 = num1+num2
        output=HttpResponse(f'sum of {num1} and {num2} is {num3}')
        return output
    
class AddTempView(TemplateView):
    template_name = "app1/add_temp.html"


class EmployeeList(ListView):
    model = Employee
    Template_name = "app1/emplist_temp.html"
    context_object_name = "qs"
