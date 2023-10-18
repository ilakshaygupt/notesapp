from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_note/',views.create_note,name="create_note"),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
    path('edit_note/<int:id>/', views.edit_note, name='edit_note'),
    path('view_note/<int:id>',views.view_note,name="view_note")
]