from .models import UserProfile, Country, Director, Actor, Genre, Movie, Rating, MovieLanguages, Moments
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name','bio')

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name','bio')

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name','description','status_movie')

@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    fields = ('language',)

@register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ('text',)
