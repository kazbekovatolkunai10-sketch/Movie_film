from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters  import SearchFilter, OrderingFilter
from rest_framework import viewsets, generics, status
from .models import (UserProfile, Country, Director, Actor, Genre, Movie, MovieLanguages, Moments,
                     Rating, Favorite,FavoriteItemMovie, History)
from .serializer import (UserProfileSerializer, CountrySerializer, DirectorSerializer, ActorSerializer,
                        GenreSerializer, MovieSerializer, MovieLanguagesSerializer, MomentsSerializer,
                        RatingSerializer, FavoriteSerializer, FavoriteItemMovieSerializer, HistorySerializer,
                         UserSerializer, LoginSerializer)
from .filter import MovieFilter
from .pagination import MovieSetPagination
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']
    pagination_class = MovieSetPagination

class MovieLanguagesListAPIView(generics.ListAPIView):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer

class MomentsListAPIView(generics.ListAPIView):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteItemMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItemMovie.objects.all()
    serializer_class = FavoriteItemMovieSerializer

class HistoryListAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
