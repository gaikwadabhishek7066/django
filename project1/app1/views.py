from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetings(request):
    str1='<h1> welcome django</h1>'
    response=HttpResponse(str1)
    return response
