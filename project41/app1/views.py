from django.shortcuts import render, redirect,HttpResponse
from app1.models import User

def singuppage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        my_user = User(username=username,password1=password1,password2=password2)
        my_user.save()
        return HttpResponse('Singup successful')
    return render(request,'app1/register.html')
    

def loginpage(request): 
    response = render(request,'app1/login.html') 
    return response
def loginview(request):
    username = request.POST['username']
    password = request.POST['Password1']
    user = User.objects.filter(username=username, password1=password)
    if len(user)!=0:
        return HttpResponse('login successful')
    else:
        return render(request,'app1/login.html', {'error': 'Invalid credentials'})
