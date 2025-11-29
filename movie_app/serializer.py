from rest_framework import serializers
from .models import (UserProfile, Country, Director, Actor, Genre, Movie, MovieLanguages,
                     Moments, Rating, Favorite,FavoriteItemMovie, History)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'last_name' ]


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'actor_name']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountryListSerializer(many=True)
    genre = GenreListSerializer(many=True)
    get_avg_rating = serializers.SerializerMethodField('get_avg_rating')
    get_count_people = serializers.SerializerMethodField('get_count_people')
    class Meta:
        model = Movie
        fields = ['id','movie_image', 'year', 'country', 'genre', 'status_movie', 'get_avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people

class DirectorDetailSerializer(serializers.ModelSerializer):
    movies_director = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Director
        fields = [ 'director_image', 'director_name', 'bio', 'age', 'movies_director']


class GenreDetailSerializer(serializers.ModelSerializer):
    movies_genre = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = ['genre_name', 'movies_genre']


class ActorDetailSerializer(serializers.ModelSerializer):
    movies_actor = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_image', 'bio', 'age', 'movies_actor']


class CountryDetailSerializer(serializers.ModelSerializer):
    countries = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Country
        fields = ['country_name', 'countries']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['id', 'language', 'video', 'movie']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie', 'movie_moments']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer(read_only=True)
    created_date = serializers.DateTimeField('%d-%m-%Y %H:%M')
    class Meta:
        model = Rating
        fields = ['user', 'created_date', 'text']


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_languages = MovieLanguagesSerializer(read_only=True, many=True)
    movie_rating = RatingSerializer(read_only=True, many=True)
    country = CountryListSerializer(many=True)
    director = DirectorListSerializer(many=True)
    genre = GenreListSerializer(many=True)
    actor = ActorListSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'movie_trailer', 'director','genre',
                  'country','actor', 'types', 'movie_time', 'description', 'movie_languages', 'movie_rating']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user']


class FavoriteItemMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItemMovie
        fields = ['cart', 'movie']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']