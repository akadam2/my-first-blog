from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=45, db_index=True, help_text='Artist name')

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=40, db_index=True, help_text="Album name")
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=40, db_index=True, help_text="Genre of music (eg: Blues)")

    def __str__(self):
        return self.name

class Tracks(models.Model):
    name = models.CharField(max_length=100, db_index=True, help_text="Track name")
    rating = models.IntegerField(null = True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
        

