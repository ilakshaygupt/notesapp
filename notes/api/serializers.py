# notes/api/serializers.py
from rest_framework import serializers
from ..models import Note  # Use ".." to go up one level to the "models" module

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content', 'picture')

class NoteDeleteSerializer(serializers.Serializer):
    pass