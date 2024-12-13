from django.shortcuts import render
from app1.forms import StudentForm
from django.http import HttpResponse

# Create your views here.

def Stud_view(request):
    if request.method == 'GET':
        stud_form = StudentForm()
        response = render(request, "app1/stud_temp.html", context={'stud_form': stud_form})
        return response
    elif request.method =='POST':
        stud_form=StudentForm(request.POST) # form object with data
        if stud_form.is_valid():
            rollno=stud_form.cleaned_data['rollno']
            name=stud_form.cleaned_data['name']
            coures=stud_form.cleaned_data['coures']
            fee=stud_form.cleaned_data['fee']
            output=f'{rollno},{name},{coures},{fee}'
            response=HttpResponse(output)
            return response
        else:
            output="Error in form data"
            response=HttpResponse(output)
            return response 


