from django.db import models

class Musician(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
      return self.name
