from django.shortcuts import render,HttpResponseRedirect
from .forms import UserRegisterForm
from .models import User
# Create your views here.

def addandshow(request):
    if request.method == 'POST':
        fm = UserRegisterForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name'] 
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            fm = UserRegisterForm()
    else:
        fm = UserRegisterForm()
    stud = User.objects.all()
    return render(request,'app1/addandshow.html', {'form':fm, 'stud':stud})


def update_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegisterForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserRegisterForm(instance=pi)
    return render(request,'app1/update.html', {'form':fm})

def delete_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')