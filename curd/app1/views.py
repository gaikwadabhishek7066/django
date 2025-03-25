from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.

def base(request):
    return render(request, 'app1/base.html')

def create(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        sub1 = request.POST.get('sub1')
        sub2 = request.POST.get('sub2')
        stud = Student(roll_no=roll_no, name=name, sub1=sub1, sub2=sub2)
        stud.save()
    response = render(request, 'app1/create.html', context={'msg':"Student create successfully"})
    return response

def create_temp(request):
    return render(request, 'app1/create.html')       
    

def list(request):
    stud = Student.objects.all()
    return render(request, 'app1/list.html', context={'stud':stud})

def delete(request):
    roll_no = request.POST.get('roll_no')
    stud = Student(roll_no=roll_no)
    stud.delete()
    return render(request, 'app1/delete.html', context={'msg':"Student delete "})

def delete_temp(request):
    return render(request, 'app1/delete.html')


def update_temp(request):
    return render(request, 'app1/update.html')

def update(request):
    if request == 'POST':
        roll_no = request.POST.get('rollo_no')
        sub1 = request.POST.get('sub1')
        sub2 = request.POST.get('sub2')
        try:
            stud = Student.objects.get(roll_no=roll_no)
            stud.sub1 = sub1
            stud.sub2 = sub2
            stud.save()
            response=render(request, 'app1/update.html', context={'msg':"updated successfully"})
        except:
            response=render(request, 'app1/update.html', context={'msg':"invalid rollno"})
        return response