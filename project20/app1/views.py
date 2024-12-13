from django.shortcuts import render
import datetime

# Create your views here.

def filter_test(request):
    num=45
    response = render(request, "app1/filter_test.html", context={'num':num})
    return response

def filter_test1(request):
    name=["abhishek", "yogesh", "thokal"]
    response = render(request, "app1/filter_test1.html", context={'name':name})
    return response

def filter_test2(request):
    dt=datetime.datetime.today()
    response = render(request, "app1/filter_test2.html", context={'dt': dt})
    return response
