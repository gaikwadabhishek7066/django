from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Users
# Create your views here.
def register(request):
    name = request.GET['name']
    uname = request.GET['uname']
    password = request.GET['password']
    u = Users(name=name,uname=uname,password=password)
    u.save()
    response = HttpResponse("User Registered...")
    return response

def signup(request):
    response = render(request, 'app1/register.html')
    return response
