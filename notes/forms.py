from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'picture']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
