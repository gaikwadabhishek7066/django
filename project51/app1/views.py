from django.shortcuts import render

# Create your views here.

def python(request):
    return render(request, 'app1/python.html')

def java(request):
    return render(request, 'app1/java.html')

def home(request):
    return render(request, 'app1/base.html')