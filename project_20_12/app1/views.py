from django.shortcuts import render
from  app1.models import *
from django.db.models import Q

# Create your views here.

def main_view(request):
    b1 =request.POST['b1']
    if b1 == 'signin':
        response = render(request, 'app1/signin.html')
        return response
    elif b1 == 'signup':
        response = render(request, 'app1/signup.html')
        return response
def home(request):
    response = render(request, 'app1/index.html')
    return response

def signup(request):
    name = request.POST['name']
    uname = request.POST['uname']
    pwd = request.POST['pwd']
    user=Users(name=name, uname=uname, password=pwd)
    try:
        user.save()
        response = render(request, 'app1/signup.html', context={'msg':"User Registered"})
        
    except:
        response = render(request, 'app1/signup.html', context={'msg':"error user register"})
        
    return response

def signin(request):
    uname = request.POST['uname']
    pwd = request.POST['pwd']
    user = Users(uname=uname, password=pwd)
    try:
        user = Users.objects.get(uname=uname, password=pwd)
        request.session['user'] = user.uname
        response = render(request, 'app1/User_dashboard.html', context={'msg':"Login Successful"})
        return response
    except:
        response = render(request, 'app1/signin.html', context={'msg':"Invalid Username or Password"})
        return response

def receive_mail(request):
    to = request.GET['to']
    message = request.GET['message']
    fr = request.session['uname']
    try:
        user = Users.objects.get(uname=to)
        mail_obj=Mails(user_from=fr,user_to=to,content=message.strip())

        mail_obj.save()
        response = render(request, 'app1/user_dashboard.html', context={'msg':'Mail Sent'})
    except:
        response = render(request, 'app1/user_dashboard.html', context={'msg': 'Error Mail sending'})
    return response

def compose_temp(request):
    response = render(request, 'app1/compose_temp.html')
    return response

def inbox_temp(request):
    uname = request.session['uname']
    qs = Mails.objects.filter(user_to=uname)
    response = render(request, 'app1/inbox_temp.html', context={'qs':qs})
    return response
def signout(request):
    if 'uname' in request.session:
        del request.session['uname']
        response=render(request,"app1/index.html")
        return response
    else:
        response=render(request,"app1/index.html")
        return response


