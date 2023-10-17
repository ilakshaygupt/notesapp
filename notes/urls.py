from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_note/',views.create_note,name="create_note"),
    path('delete/<int:id>/', views.delete_note, name='delete_note')

]

