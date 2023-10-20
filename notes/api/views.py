from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer, Note



@api_view(['GET'])
def notes(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createnotes(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def readnotes(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note)
    return Response(serializer.data)


@api_view(['GET', 'PUT','POST'])
def updatenotes(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def deletenotes(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Deleted Successfully")