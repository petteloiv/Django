from .models import Actor, Movie, Review
from rest_framework import serializers

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class MovieForActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)
    movies = MovieForActorSerializer(many=True)

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieSerializer(serializers.ModelSerializer):
    class ActorForMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewForMovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('title', 'content',)

    actors = ActorForMovieSerializer(many=True)
    review_set = ReviewForMovieSerializer(many=True)
    

    class Meta:
        model = Movie
        fields = '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)
        read_only_fields = ('movie',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieForReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieForReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content',)
