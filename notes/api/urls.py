# notes/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='note-create'),
    path('notes/update/<int:pk>/', views.NoteUpdate.as_view(), name='note-update'),
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='note-delete'),
]
