from django.shortcuts import render,HttpResponse
from .models import it
# Create your views here.

def listview(request):
    name = request.POST.get('name')
    course = request.POST.get('course')
    fees = request.POST.get('fees')
    data = it(name=name, course=course, fees=fees)
    data.save()
    return render(request,'app1/add.html',context={'msg':'Student Added...'})

def list(request):
    return render(request, 'app1/add.html')