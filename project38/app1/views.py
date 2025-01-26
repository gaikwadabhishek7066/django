from django.shortcuts import render, redirect
from app1.models import User,Login
from app1.forms import UserCreateForm,AuthenticationForm

# Create your views here.
def register_view(request):
 if request.method == 'POST':
  form = UserCreateForm(request.POST)
  if form.is_valid():
   user= form.save()
   Login(request, user)
   return redirect('dashboard')
 else:
  form = UserCreateForm()
  return render(request,'app1/register.html', {'form': form})

def login_view(request):
 if request.method == 'POST':
  form = AuthenticationForm(request.POST)
  if form.is_valid():
   user = form.get_user()
   Login(request, user)
   return redirect('dashboard')
 else:
  initial_data = {'username':'', 'password':''}
  form = AuthenticationForm(initial=initial_data)
 return render(request,'app1/login.html', {'form': form})

def dashboard_view(request):
 return render(request, 'app1/dashboard.html')

def logout_view(request):
 Login(request)
 return redirect('login')
 