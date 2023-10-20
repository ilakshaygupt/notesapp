from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from ..models import Note
from .serializers import NoteSerializer , NoteDeleteSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteCreate(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    parser_classes = (MultiPartParser, FormParser)

class NoteUpdate(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer 
    parser_classes = (MultiPartParser, FormParser)

class NoteDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteDeleteSerializer 
