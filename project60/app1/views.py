from django.shortcuts import render
from app1.models import *
from django.db.models import Q
# Create your views here.

def main_view(request):
    b=request.GET['b']
    if b == 'signin':
        response=render(request,'app1/signin.html')
    elif b== 'signup':
        response=render(request,'app1/signup.html')
    return response

def home(request):
    return render(request,'app1/index.html')

def signup(request):
    name = request.POST['name']
    uname =request.POST['uname']
    password = request.POST['password']
    user = Users(name=name,uname=uname,password=password)
    try:
        user.save()
        response = render(request,'app1/index.html',context={'msg':'User Registered...'})
    except:
        response = render(request,'app1/signup.html',context={'msg':'Error Registered user'}) 
    return response

def signin(request):
    uname =request.POST['uname']
    password = request.POST['password']
    try:
        user=Users.objects.get(Q(uname=uname)&Q(password=password))
        response = render(request,'app1/dashboard.html',context={'request':request})
        request.session['uname']=uname
    except:
        msg="Invalid UserName or Password"
        response=render(request,'app1/signin.html',context={'msg':msg})
    return response

def receive_mail(request):
    to=request.GET['to']
    message=request.GET['message']
    fr=request.session['uname']
    try:
         user=Users.objects.get(uname=to)
         mail_obj=Mail(from_user=fr,to_user=user,content=message.strip())
        
         mail_obj.save()
         response=render(request,"app1/dashboard.html",context={'msg':'Mail Sent'})
    except:
        response=render(request,"app1/dashboard.html",context={'msg':'Error in sending message'})
    return response

def compose_temp(request):
    rensponse = render(request,'app1/compose_temp.html')
    return rensponse

def inbox(request):
    uname = request.session['uname']
    qs = Mail.objects.filter(to_user=uname)
    response = render(request,'app1/inbox.html',context={'qs':qs})
    return response

def signout(request):
    if 'uname' in request.session:
        del request.session['uname']
        response=render(request,"app1/index.html")
        return response
    else:
        response=render(request,"app1/index.html")
        return response

