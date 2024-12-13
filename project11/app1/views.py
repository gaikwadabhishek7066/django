from django.shortcuts import render

# Create your views here.

def index(request):
    response = render(request, "app1/index.html")
    return response

def student_result(request):
    stud_data = {
        'abhi': [90,98],
        'yogesh':[99,97],
        'thokal':[39,78]
    }
    response = render(request, "app1/student_result.html", context={'stud_data':stud_data})
    return response