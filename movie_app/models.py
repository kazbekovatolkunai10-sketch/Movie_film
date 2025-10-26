from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
)

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(12),MaxValueValidator(100)], null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class Country(models.Model):
   country_name = models.CharField(max_length=100, unique=True)

   def __str__(self):
       return f'{self.country_name}'

class Director(models.Model):
    director_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
    director_image = models.ImageField(upload_to='director_image/', null=True, blank=True)

    def __str__(self):
        return f'{self.director_name},{self.bio},{self.age},{self.director_image}'

class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],  null=True, blank=True)
    actor_image = models.ImageField(upload_to='actor_image/', null=True, blank=True)

    def __str__(self):
        return f'{self.actor_name},{self.bio},{self.age},{self.actor_image}'

class Genre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.genre_name}'

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    year = models.DateField()
    country =  models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPES_CHOICES = (
        ('140p','140p'),
        ('360p','360p'),
        ('480p','480p'),
        ('720p','720p'),
        ('1080p','1080p'),
    )
    types = models.CharField(max_length=24, choices=TYPES_CHOICES, default='480p')
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer/')
    movie_image = models.ImageField(upload_to='movie_photo/')
    status_movie = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return (f'{self.movie_name},{self.year},{self.types},{self.movie_time}'
                f'{self.director},{self.actor},{self.genre},{self.types},{self.movie_trailer}'
                f'{self.description},{self.movie_image},{self.status_movie}')

class MovieLanguages(models.Model):
    language = models.CharField(max_length=42)
    video = models.FileField(upload_to='movie_video/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.language},{self.video},{self.movie}'


class Moments(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  movie_moments = models.ImageField(upload_to='movie_moments/')

  def __str__(self):
      return f'{self.movie},{self.movie_moments}'

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,11)],
                                             null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.movie},{self.stars},{self.text},{self.created_date}'


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class FavoriteItemMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart},{self.movie}'

class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.movie},{self.viewed_at}'


