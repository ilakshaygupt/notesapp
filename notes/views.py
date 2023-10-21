from django.views.generic import CreateView, DeleteView, UpdateView, ListView ,FormView
from .models import Note
from .forms import NoteForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
class CustomLoginView(LoginView):
    template_name = 'notes/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'
    
class RegisterPage(FormView):
    template_name = 'notes/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = '/'

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage,self).get(*args,**kwargs)
class CustomLogoutView(LogoutView):
    template_name = 'notes/logout.html'
    fields = '__all__'

    def get_success_url(self):
        return '/login/'
class HomeView(LoginRequiredMixin,ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    paginate_by = 10 

    # def get_queryset(self):
    #     search_query = self.request.GET.get('search_query')
    #     if search_query:
    #         return Note.objects.filter(title__icontains=search_query)
    #     return Note.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.all().filter(user=self.request.user)
        if self.request.GET.get('search_query'):
            context['notes'] = Note.objects.filter(title__icontains=self.request.GET.get('search_query'))
        return context

class CreateNoteView(LoginRequiredMixin,CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNoteView, self).form_valid(form)

class ViewNoteView(LoginRequiredMixin,UpdateView):
    model = Note
    fields = ['title', 'content', 'picture']
    template_name = 'notes/view_note.html'
    

class DeleteNoteView(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = '/'
    template_name = 'notes/delete_note.html'
    

class UpdateNoteView(LoginRequiredMixin,UpdateView):
    model = Note
    fields = ['title', 'content', 'picture']
    template_name = 'notes/edit_note.html'
    success_url = '/'
