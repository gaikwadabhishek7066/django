from django.shortcuts import render
from app1.forms import*
from django.http import HttpResponse

# Create your views here.

def get_temp(request):
    regfrm=RegisterForm()
    response = render(request, "app1/gettext.html", context={'regfrm': regfrm})
    return response

def post_temp(request):
    regfrm=RegisterForm()
    response = render(request, "app1/posttext.html", context={'regfrm': regfrm})
    return response

def getview(request):
    msg="this is a get request"
    response=HttpResponse(msg)
    return response

def postview(request):
    msg="thos is a post request"
    response=HttpResponse(msg)
    return response

def home_temp(request):
    response=render(request, "app1/index.html")
    return response
