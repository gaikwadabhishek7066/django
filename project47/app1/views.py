from django.shortcuts import render

# Create your views here.
def singin_view(request):
    users = {'nit':'n123',
             'abhi':'a123',
             'yogesh':'y123'}
    uname = request.GET['uname']
    pwd = request.GET['pwd']
    if uname in users and users [uname]==pwd:
        response = render(request, 'app1/welcome.html', context={'uname':uname})
        return response
    else:
        response = render(request, 'app1/login.html',context={'msg':"Invalid username and password"})
        return response
    
def login(request):
    return render(request, 'app1/login.html')