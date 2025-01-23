from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def get_temp(request):
    reform=RegisterForm
    response = render(request, 'app1/gettest.html', context={'refrom':reform})
    return response

def post_temp(request):
    reform = RegisterForm
    response = render(request, 'app1/posttest.html', context={'reform':reform})
    return response

def getview(request):
    msg = "This is  get request"
    response=HttpResponse(msg)
    return response

def postview(request):
    msg = "This is  post request"
    response=HttpResponse(msg)
    return response
def home_temp(request):
    response=render(request, 'app1/index.html')
    return response