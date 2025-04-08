from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    return render(request, 'data/home.html')

def addview(request):
    if request.method== 'POST':
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        stud = Student(roll_no=roll_no, name=name, marks=marks)
        stud.save()
        msg = "Student added successfully"
    else:
        msg = "Invalid data"
    return render(request, 'data/add.html', context={'msg':msg})
    
def add_temp(request):
    return render(request, 'data/add.html')

def listview(request):
    stud = Student.objects.all()
    return render(request, 'data/list.html',context={'stud':stud})