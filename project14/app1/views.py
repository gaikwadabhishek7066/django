from django.shortcuts import render

# Create your views here.

def python(request):
    response = render(request, 'app1/python.html')
    return response

def java(request):
    response = render(request, 'app1/java.html')
    return response

def home(request):
    response = render(request, 'app1/base.html')
    return response