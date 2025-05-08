from django.shortcuts import render

# Create your views here.
student_data={}

def home(request):
    return render(request, 'app1/index.html')

def student_add(request):
    name = request.GET['name']
    course = request.GET['course']
    fees = request.GET['fees']
    student_data[name]=[course,fees]
    return render(request, 'app1/index.html', context={'msg':'Student Added...'})
def display_student(request):
    return render(request, 'app1/display_student.html',context={'student_data':student_data})

def add_temp(request):
    return render(request, 'app1/add_student.html')