from django.shortcuts import render
from app1.models import Users
# Create your views here.

def register(request):
    name = request.GET['name']
    uname = request.GET['uname']
    password = request.GET['password']
    u = Users(name=name,uname=uname,password=password)
    u.save()
    response = render(request, 'app1/register.html', context={'msg':"user registered"})
    return response

def home(request):
    response = render(request, 'app1/register.html')
    return response

def display_users(request):
    qs = Users.objects.all()
    response = render(request, 'app1/display.html',context={'qs':qs})
    return response
