"""
URL configuration for project62 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('add/',add_student),
    path('add_temp/',add_student_temp),
    path('update/',update_student),
    path('update_temp/',update_student_temp),
    path('delete/',delete_student),
    path('delete_temp/',delete_student_temp),
    path('find/',find_result),
    path('find_temp/',find_result_temp),
    path('view/',view_students)
]
