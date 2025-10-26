from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileViewSet, CountryListAPIView, DirectorListAPIView, ActorListAPIView,
                    GenreListAPIView, MovieViewSet, MovieLanguagesListAPIView, MomentsListAPIView,
                    RatingViewSet, FavoriteViewSet, FavoriteItemMovieViewSet, HistoryListAPIView,
                    RegisterView, LogoutView, CustomLoginView)

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite_items', FavoriteItemMovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('countries', CountryListAPIView.as_view(), name='countries'),
    path('directors', DirectorListAPIView.as_view(), name='directors'),
    path('actors', ActorListAPIView.as_view(), name='actors'),
    path('genres', GenreListAPIView.as_view(), name='genres'),
    path('movie_language', MovieLanguagesListAPIView.as_view(), name='movie_language'),
    path('moments', MomentsListAPIView.as_view(), name='moments'),
    path('history', HistoryListAPIView.as_view(), name='history'),
]