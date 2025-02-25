from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)
    album_art = models.ImageField(upload_to='')
    release_date = models.DateField()
    average_rating = models.FloatField()
    links = models.URLField()

    def __str__(self):
        return self.album_name

    def genre_list(self):
        return list(self.genre.values_list('genre', flat=True))

    def artist_list(self):
        return list(artist.name for artist in self.artists.all())


class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_writer = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    news_detail = models.TextField()
    news_image = models.ImageField(upload_to='')

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = 'News'


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.album} - {self.rating}"

    class Meta:
        verbose_name_plural = 'Reviews'