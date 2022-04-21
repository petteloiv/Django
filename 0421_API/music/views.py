from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicSerializer, MusicDetailSerializer
from music import serializers
# Create your views here.


@api_view(['GET', 'POST'])
def artist_list_create(request):
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializers = ArtistListSerializer(artists, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE'])
def artist_detail_delete(request, artist_pk):

    artist = get_object_or_404(Artist, pk=artist_pk)

    if request.method == 'GET':
        serializers = ArtistSerializer(artist)
        return Response(serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'delete': f'{artist_pk}번째 게시글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def music_list(request):
    music = get_list_or_404(Music)
    serializer = MusicSerializer(music, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT','DELETE'])
def music_detail_update(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)

    if request.method == 'GET':
        serializer = MusicDetailSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicDetailSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'{music_pk}번째 음악이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
