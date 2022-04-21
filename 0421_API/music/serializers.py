from rest_framework import serializers
from .models import Artist, Music


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'

# 읽기 전용
class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)

# 더 자세히! 한 단계 더 들어가서! 
class MusicDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
        depth = 1

# 종속 되어 있는 애 불러오기 
class ArtistSerializer(serializers.ModelSerializer):
    class MusicSerializerForArtist(serializers.ModelSerializer):

        class Meta:
            model = Music
            fields = ('title',)

    music_set = MusicSerializerForArtist(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count')