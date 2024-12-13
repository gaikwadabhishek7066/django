from django.shortcuts import render

# Create your views here.
students_data={}
def home(request):
    response = render(request, 'app1/index.html')
    return response

def add_student(request):
    name = request.GET['name']
    course = request.GET['course']
    fees = request.GET['fees']
    students_data[name] = [course,fees]
    response = render(request, "app1/index.html", context={"msg": "studentadded"})
    return response
                  
def display_student(request):
    response = render(request, "app1/display_student.html", context={'students_data':students_data})
    return response

def add_templates(request):
    response = render(request, "app1/add_student.html")
    return response