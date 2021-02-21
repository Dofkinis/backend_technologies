from django.shortcuts import render
from django.views.generic import ListView, CreateView
from movies.models import Movie, Actor


class MoviesListView(ListView):
    model = Movie
    context_object_name = 'movies_list'


class ActorListView(ListView):
    model = Actor
    context_object_name = 'actor_list'


# Movie(title, actor, lenght, description
class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'actor', 'lenght', 'description']

# Actor(name, last_name)
class ActorCreateView(CreateView):
    model = Actor
    fields = ['name', 'last_name']
    # fields = "__all__"
