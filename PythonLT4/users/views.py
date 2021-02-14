from django.shortcuts import render, HttpResponse
from . models import User, Lobby
from django.views.generic import CreateView
from . forms import CreateUserForm
from django.urls import reverse_lazy

# Create your views here.
def hello(request, user):
    return HttpResponse(f'Hello, {user}')


def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/index.html', context=context)


def lobbies(request):
    # list lobbies and their users
    lobbies = Lobby.objects.all()
    context = {'lobbies': lobbies}
    return render(request, 'users/lobbies.html', context=context)


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('lobbies')
