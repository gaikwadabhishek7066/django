from django.shortcuts import render
from django.http import HttpResponse
from app1.models import User
# Create your views here.

def index(request):
    response = render(request, 'app1/index.html')
    return response

def signup_view(request):
    name = request.GET['name']
    uname = request.GET['uname']
    pwd = request.GET['pwd']
    user = User(name=name, uname=uname, pwd=pwd)
    user.save()
    response = render(request, 'app1/signup_temp.html', context={'msg': "User Registered..."})
    return response
def home(request):
    response = render(request, 'app1/signup_temp.html')
    return response

def signin_view(request):
    uname = request.GET['uname']
    pwd = request.GET['pwd']
    user = User.objects.filter(uname=uname, pwd=pwd)
    response = render(request, 'app1/home_temp.html',context={'uname':uname})
    return response
def signin(request):
    response = render(request,'app1/signin_temp.html')
    return response
    
def change_password(request):
    uname = request.GET['uname']
    old_pwd = request.GET['old_pwd']
    new_pwd = request.GET['new_pwd']
    user = User.objects.filter(uname=uname, pwd=old_pwd)
    if user:
        user.update(pwd=new_pwd)
        response = render(request, 'app1/home_temp.html', context={'uname':uname})
    else:
        response = render(request, 'app1/home_temp.html', context={'uname':uname, 'error':"Invalid Password"})
    return response

def change(request):
    response = render(request,'app1/change_password_temp.html',context={'msg':"change password successfully"})
    return response