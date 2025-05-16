from django.shortcuts import render
from .models import Form
# Create your views here.
def form_view(request):
    name = request.GET['name']
    email = request.GET['email']
    loginid = request.GET['loginid']
    password = request.GET['password']
    number = request.GET['number']
    form = Form(name=name, email=email,loginid=loginid,password=password,number=number)
    form.save()
    return render(request, 'app1/form.html', context={'msg':"Register successfully..."})


def view(request):
    return render(request, 'app1/form.html')


def list_form(request):
    form = Form.objects.all()
    return render(request, 'app1/list.html', context={'form':form})