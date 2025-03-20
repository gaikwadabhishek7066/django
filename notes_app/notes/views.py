from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import  NoteForm

# Create your views here.

@login_required
def notes_list(request):
    notes = Note.objects.filter(user = request.user)
    return render(request, 'notes/notes_list.html',{'notes':notes})

@login_required
def note_create(request):
    if request.method =='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form':form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html',{'form':form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'notes/note_confirm_delete.html', {'note':note})