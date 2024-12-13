from django.shortcuts import render

# Create your views here.

def list_students(request):
    student_data = {101:['dhoni', 'python', 'MS-Dhoni-3.jpeg'],
                     102:['rohit', 'java', 'rohit-sharma.webp'],
                     103:['virat', '.net', 'Virat-Kohli.webp']}
    
    response = render(request, 'app1/list_students.html', context={'student_data': student_data})
    return response