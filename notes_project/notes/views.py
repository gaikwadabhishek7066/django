from django.shortcuts import render, get_object_or_404,redirect
from .models import Note
from .forms import NoteForm

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes':notes})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form':form})

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method =='POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form':form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('index')