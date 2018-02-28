from django.db import models
from django.core.urlresolvers import  reverse

# Create your models here.

class Album(models.Model):
    Artist= models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    Genere= models.CharField(max_length=250)
    album_logo = models.FileField(null=True)

    def __str__(self):
        return  self.album_title + ' \n  ' + self.Artist

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk':self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length= 10)
    song_title = models.CharField(max_length= 500)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
