from rest_framework import serializers
from .models import (UserProfile, Country, Director, Actor, Genre, Movie,
                     MovieLanguages, Moments, Rating, Favorite,
                     FavoriteMovie, History)
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
        fields = ['first_name', 'last_name']


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
        fields = ['actor_name']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['gere_name']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountryListSerializer(many=True)
    genre = GenreListSerializer(many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'year', 'country',
                  'genre', 'status_movie', 'get_avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()



class GenreDetailSerializer(serializers.ModelSerializer):
    movie_genre = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = ['gere_name', 'movie_genre']


class ActorDetailSerializer(serializers.ModelSerializer):
    movie_actor = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Actor
        fields = ['actor_image', 'actor_name', 'bio', 'age', 'movie_actor']


class CountryDetailSerializer(serializers.ModelSerializer):
    movie_countries = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Country
        fields = ['country_name', 'movie_countries']


class DirectorDetailSerializer(serializers.ModelSerializer):
    movies_director = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Director
        fields = ['director_image', 'director_name', 'bio', 'age', 'movies_director']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['id', 'language', 'video']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format=('%d-%m-%Y %H:%M'))
    class Meta:
        model = Rating
        fields = ['user', 'created_date', 'text']


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_language = MovieLanguagesSerializer(read_only=True, many=True)
    review_movie = RatingSerializer(read_only=True, many=True)
    country = CountryListSerializer(many=True)
    director = DirectorListSerializer(many=True)
    genre = GenreListSerializer(many=True)
    actor = ActorListSerializer(many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_image', 'movie_trailer', 'movie_name', 'status_movie','year', 'country', 'director',
                  'genre', 'types', 'movie_time', 'actor', 'description', 'movie_language', 'get_avg_rating', 'get_count_people', 'review_movie']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


