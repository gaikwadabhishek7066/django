from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'app1/task_list.html', {'tasks':tasks})

def add_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect("task_list")
    return redirect("task_list")

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("task_list")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")
