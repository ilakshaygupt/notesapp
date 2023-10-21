from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Note
from .forms import NoteForm

class HomeView(ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    paginate_by = 10 

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        if search_query:
            return Note.objects.filter(title__icontains=search_query)
        return Note.objects.all()

class CreateNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = '/'

class ViewNoteView(UpdateView):
    model = Note
    fields = ['title', 'content', 'picture']
    template_name = 'notes/view_note.html'
    

class DeleteNoteView(DeleteView):
    model = Note
    success_url = '/'
    template_name = 'notes/delete_note.html'
    

class UpdateNoteView(UpdateView):
    model = Note
    fields = ['title', 'content', 'picture']
    template_name = 'notes/edit_note.html'
    success_url = '/'
