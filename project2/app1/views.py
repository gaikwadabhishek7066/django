from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# 
def home(request):
    output='''<html>
    <body bgcolor=cyan color=bule>
    <h1> this is a page</h1>
    </body></html>'''
    response=HttpResponse(output)
    return response
