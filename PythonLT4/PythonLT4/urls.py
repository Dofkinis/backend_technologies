"""PythonLT4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import hello, index, lobbies
from users.views import CreateUserView
from movies.views import MoviesListView, ActorListView, MovieCreateView, ActorCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('hello/<user>', hello),
    path('lobbies/', lobbies, name='lobbies'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('movies/', MoviesListView.as_view(), name='movies'),
    path('actors/', ActorListView.as_view(), name='actors'),
    path('create-movie/', MovieCreateView.as_view(), name='create-movie'),
    path('create-actor/', ActorCreateView.as_view(), name='create-actor'),
]
