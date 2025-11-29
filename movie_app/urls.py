from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CountryListAPIView, DirectorListAPIView, DirectorDetailAPIView,
                    ActorListAPIView, CountryDetailAPIView,
                    GenreListAPIView, MovieListAPIView, MovieDetailAPIView, MovieLanguagesListAPIView,
                    MomentsListAPIView,
                    RatingViewSet, FavoriteViewSet, FavoriteItemMovieViewSet, HistoryListAPIView,
                    RegisterView, LogoutView, CustomLoginView, ActorDetailAPIView, GenreDetailAPIView)

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite_items', FavoriteItemMovieViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('countries', CountryListAPIView.as_view(), name='countries'),
    path('directors', DirectorListAPIView.as_view(), name='directors'),
    path('actors', ActorListAPIView.as_view(), name='actors'),
    path('genres', GenreListAPIView.as_view(), name='genres'),
    path('movie_language', MovieLanguagesListAPIView.as_view(), name='movie_language'),
    path('moments', MomentsListAPIView.as_view(), name='moments'),
    path('history', HistoryListAPIView.as_view(), name='history'),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('director/', DirectorListAPIView.as_view(), name='director-list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor-list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre-list'),
    path('genre/<int:pk>', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('countries/', CountryListAPIView.as_view(), name='country-list'),
    path('countries/<int:pk>', CountryDetailAPIView.as_view(), name='country-detail'),
]