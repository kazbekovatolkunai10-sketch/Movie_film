from rest_framework import routers
from django.urls import path, include
from .views import (UserProfileViewSet, CountryListAPIView, CountryDetailAPIView, DirectorListAPIView, DirectorDetailAPIView,
                    ActorListAPIView, ActorDetailAPIView, GenreListAPIView, GenreDetailAPIView,
                    MovieListAPIView, MovieDetailAPIView, MovieLanguagesViewSet, MomentsViewSet,
                    RatingViewSet, FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, RegisterView, CustomLoginView, LogoutView)

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'movie_language', MovieLanguagesViewSet)
router.register(r'moment', MomentsViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_movie', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('director/', DirectorListAPIView.as_view(), name='director-list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('country/', CountryListAPIView.as_view(), name='country-list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor-list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre-list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail')
]




