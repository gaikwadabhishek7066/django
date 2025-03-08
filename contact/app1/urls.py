from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),

    path('add/', views.add_contact, name='add_contact'),
    path('update/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
