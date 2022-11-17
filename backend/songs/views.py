from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Song
from .serializers import SongSerializer


@api_view(['GET', 'PUT', 'POST'])
def songs_by_request(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'DELETE'])
def songs_by_id(request, pk):
    song = Song.objects.filter(pk=pk)
    serializer = SongSerializer(song, many=True)
    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)