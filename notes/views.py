from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from .forms import NoteForm


def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
def delete_note(request,id):
    if request.method=='POST':
        note = get_object_or_404(Note, id=id)
        note.delete()
        return redirect('home')


def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()  # Update the existing note with the edited data
            return redirect('home')
    else:
        form = NoteForm(instance=note)  # Pre-fill the form with existing data

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})
