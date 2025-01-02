from django.shortcuts import render
from app1.models import Student
from django.http import HttpResponse
# Create your views here.

def add_view(request):
    rollno = request.GET['rollno']
    name = request.GET['name']
    sub1 = request.GET['sub1']
    sub2 = request.GET['sub2']
    student = Student(rollno=rollno,name=name,sub1=sub1,sub2=sub2)
    student.save()
    response = render(request, 'app1/student_add.html', {'msg':"Student added..."})
    return response

def add(request):
    response = render(request, 'app1/student_add.html')
    return response
def home(request):
    response = render(request, 'app1/home.html')
    return response

def update_view(request):
    rollno = request.GET['rollno']
    sub1 = request.GET['sub1']
    sub2 = request.GET['sub2']
    try:
        s=Student.objects.get(rollno=rollno)
        s.sub1=sub1
        s.sub2=sub2
        s.save()
        response = render(request, 'app1/student_update.html', context={'msg':"Student Updated..."})
        return response
    except:
        response = render(request, 'app1/student_update.html', context={'msg':"Invalid Student Updated..."})
        return response
    
def update(request):
    response=render(request, 'app1/student_update.html')
    return response

def find_result_view(request):
    rollno = request.GET['rollno']
    try:
        s=Student.objects.filter(rollno=rollno)
        response = render(request, 'app1/result.html', context={'s':s})
        return response
    except:
        response = render(request, 'app1/find_result.html', context={'msg':"Invalid Rollno pls try again "})
        return response
        
def find_result(request):
    response = render(request, 'app1/find_result.html')
    return response

def delete_view(request):
    rollno = request.GET['rollno']
    try:
        s=Student.objects.get(rollno=rollno)
        s.delete()
        response = render(request, 'app1/delete.html', context={'msg':"Student Deleted..."})
        return response
    except:
        response = render(request, 'app1/delete.html', context={'msg':"Invalid Rollno pls try again "})
        return response
    
def delete(request):
    response = render(request, 'app1/delete.html')
    return response

def student_view(request):
    s=Student.objects.all()
    response = render(request, 'app1/student.html', context={'s':s})
    return response
