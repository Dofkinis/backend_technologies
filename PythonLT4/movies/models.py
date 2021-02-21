from django.db import models
from django.urls import reverse

# Tables: Movie, Actor
# Fields: Movie(title, actor, lenght, description), Actor(name, last_name)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actor = models.ManyToManyField('Actor')
    lenght = models.IntegerField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('movies')


class Actor(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('actors')

    def __str__(self):
        return self.name + ' ' + self.last_name
