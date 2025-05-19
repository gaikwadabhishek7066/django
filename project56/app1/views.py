from django.shortcuts import render
from . models import User
from django.db.models import Q
# Create your views here.
def sign_up(request):
    name = request.GET['name']
    phone  =request.GET['phone']
    email = request.GET['email']
    pwd = request.GET['pwd']
    user = User(name=name,phone=phone,email=email,pwd=pwd)
    user.save()
    return render(request, 'app1/singup.html', context={'msg':"SignUP successfully..."})

def sign_temp(request):
    return render(request, 'app1/singup.html')

def sign_view(request):
    return render(request, 'app1/singup.html')

def login(request):
    return render(request, 'app1/singin.html')

def signin_view(request):
    email = request.GET['email']
    pwd = request.GET['pwd']
    qs = User.objects.filter(Q(email=email) & Q(pwd=pwd))
    if len(qs)==0:
        return render(request, 'app1/singin.html', context={'msg':"Invalid Username and Password..."})
    else:
        return render(request, 'app1/welcome.html',context={'email':email})

        
