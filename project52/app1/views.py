from django.shortcuts import render

# Create your views here.
def list_stud(request):
    student_data={101:['dhoni','python','dhoni.jpeg'],
                  102:['rohit','java','rohit.webp'],
                  103:['virat','.net','virat.jpg']
                  }
    return render(request, 'app1/list_stud.html', context={'student_data':student_data})
