from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app1/index.html')

def student_result(request):
    stud_data={
        'abhi':[80,90],
        'yogesh':[90,95],
        'narayan':[35,50],
        'shubham':[60,70]
    }
    return render(request, 'app1/result.html', context={'stud_data':stud_data})