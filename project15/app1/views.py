from django.shortcuts import render

# Create your views here.

def read_data(request):
    n1 = eval(request.GET['num1'])
    n2 = eval(request.GET['num2'])
    n3 = n1+n2
    response = render(request, "app1/add.html", context={'n1': n1, 'n2': n2, 'n3': n3})
    return response

def home(request):
    response = render(request, "app1/home.html")
    return response