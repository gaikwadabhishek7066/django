from django.urls import path
from .views import notes_list,note_create,note_edit,note_delete

urlpatterns = [
    path('',notes_list, name='notes_list'),
    path('new/',note_create, name='note_create'),
    path('<int:pk>/edit/',note_edit,name='note_edit'),
    path('<int:pk>/delete/',note_delete, name='note_delete'),

]