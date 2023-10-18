from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm,SearchForm
from .models import Note


def home(request):
    notes = Note.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        if search_query:
            notes = Note.objects.filter(title__icontains=search_query)
        
    return render(request, 'notes/home.html', {'notes': notes, 'search_form': search_form})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
def view_note(request,id):
    note = get_object_or_404(Note, id=id)#404 page error if model not foun
    return render(request, 'notes/view_note.html', {'note': note})

def delete_note(request,id):
    if request.method=='POST':
        note = get_object_or_404(Note, id=id)
        note.delete()
        return redirect('home')#redirect to url absoulte or base url


def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})
