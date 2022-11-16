from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Song
from .serializers import SongSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_songs(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
def songs_by_id(request, pk):
    song = Song.objects.filter(pk=pk)
    serializer = SongSerializer(song, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)