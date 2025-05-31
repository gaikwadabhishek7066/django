from django.shortcuts import render,redirect
from django.http import HttpResponse 
from app1.forms import SignupForm


# Create your views here.
def welcome(request):
    output = "<h2>Hello Welcome</h2>"
    response=HttpResponse(output)
    return response