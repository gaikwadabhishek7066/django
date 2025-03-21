from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register

urlpatterns = [
    path('register/', register,name='register'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout')
]