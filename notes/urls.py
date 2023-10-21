from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('create_note/', views.CreateNoteView.as_view(), name='create_note'),
    path('delete/<int:pk>/', views.DeleteNoteView.as_view(), name='delete_note'),
    path('edit_note/<int:pk>/', views.UpdateNoteView.as_view(), name='edit_note'),
    path('view_note/<int:pk>/', views.ViewNoteView.as_view(), name='view_note'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
