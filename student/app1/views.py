from django.shortcuts import render
from app1.models import User,Student
# Create your views here.


def home(request):
    return render(request, 'app1/singup.html')
def singup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(name=name, username=username, password=password)
        user.save()
    return render(request, 'app1/singup.html', context={'msg':"Successfully created"})

def signin(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            return render(request, 'app1/home.html')
        else:
            return render(request, 'app1/singin.html', context={'msg':"Invalid credentials"})
     return render(request, 'app1/singin.html')

def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email =request.POST.get('email')
        age = request.POST.get('age')
        student = Student(name=name, roll_number=roll_number, email=email, age=age)
        student.save()
    return render(request, 'app1/addstudent.html', context={'msg':"Student added successfully"})

def viewstudents(request):
    students = Student.objects.all()
    return render(request, 'app1/showstudent.html', context={'students':students})