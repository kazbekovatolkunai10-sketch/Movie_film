from django_filters.rest_framework import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country': ['exact'],
            'year': ['gt', 'lt'],
            'genre' : ['exact'],
            'status_movie': ['exact'],
            'actor': ['exact'],
            'director':['exact']
        }