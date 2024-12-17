from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login_view(request):
    uname = request.GET['user']
    response = render(request, "app1/inbox.html")
    response.set_cookie("uname",uname)
    return response

def inbox_view(request):
    uname = request.COOKIES['uname']
    output = f'''
        <h1>{uname}</h1>,
        <h1> this is inbox </h1>'''
    response = HttpResponse(output)
    return response

def Home(request):
    response = render(request, "app1/login.html")
    return response9021158763