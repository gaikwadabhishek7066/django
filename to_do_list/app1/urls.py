from django.urls import path
from .views import task_list,add_list, complete_task,delete_task

urlpatterns = [
    path('',task_list, name='task_list'),
    path('add/',add_list, name='add_list'),
    path('complete/<int:task_id>/',complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),

]