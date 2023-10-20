from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.notes, name="notes"),
    path('createnote/',views.createnotes, name="createnote"),
    path('readnote/<str:pk>/', views.readnotes, name="readnote"),
    path('updatenote/<str:pk>/', views.updatenotes, name="updatenote"),
    path('deletenote/<str:pk>/', views.deletenotes, name="deletenote"),
]
