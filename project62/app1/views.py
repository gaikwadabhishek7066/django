from django.shortcuts import render
from app1.models import Marks
# Create your views here.

def home(request):
    return render(request, 'app1/index.html')

def add_student(request):
    rno = int(request.GET['rno'])
    name = request.GET['name']
    s1 = float(request.GET['sub1'])
    s2 = float(request.GET['sub2'])
    m = Marks(rollno=rno,name=name,sub1=s1,sub2=s2)
    m.save()
    return render(request, 'app1/add_student.html',context={'msg':'Student Added'})

def add_student_temp(request):
    return render(request, 'app1/add_student.html')

def update_student(request):
    rno = int(request.GET['rno'])
    s1 = float(request.GET['sub1'])
    s2 = float(request.GET['sub2'])
    try:
        stud = Marks.objects.get(rollno=rno)
        stud.sub1=s1
        stud.sub2=s2
        stud.save()
        response = render(request, 'app1/update_student.html',context={'msg':'Marks Updated'})
    except:
        response = render(request, 'app1/update_student.html',context={'msg':'Invalid Rollno'})
    return response

def update_student_temp(request):
    return render(request,'app1/update_student.html')

def delete_student(request):
    rno = int(request.GET['rno'])
    try:
        stud = Marks.objects.get(rollno=rno)
        stud.delete()
        rensponse = render(request, 'app1/delete_student.html',context={'msg':'Student Deleted'})
    except:
        rensponse = render(request, 'app1/delete_student.html',context={'msg':'Invalid Rollno'})
    return rensponse

def delete_student_temp(request):
    return render(request, 'app1/delete_student.html')


def find_result(request):
    rno = int(request.GET['rno'])
    try:
        stud = Marks.objects.get(rollno=rno)
        result = "PASS" if stud.sub1>=40 and stud.sub2>=40 else "FAIL"
        rensponse = render(request, 'app1/show_result.html',context={'stud':stud,"result":result})
    except:
        rensponse = render(request, 'app1/find_result.html',context={'msg':'invalid rno'})
    return rensponse

def find_result_temp(request):
    return render(request, 'app1/find_result.html')

def view_students(request):
    qs = Marks.objects.all()
    return render(request, 'app1/show_student.html', context={'qs':qs})