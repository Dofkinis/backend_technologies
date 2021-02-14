from django.db import models

# Create your models here.
class User(models.Model):
    gender_choices = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    name = models.CharField(verbose_name='Vardas', max_length=100)
    last_name = models.CharField(verbose_name='Pavardė', max_length=100, null=True)
    email = models.EmailField(verbose_name='El. paštas', max_length=100, null=True)
    gender = models.CharField(verbose_name='Lytis', max_length=15, choices=gender_choices, null=True)
    description = models.TextField('Description about you', max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lobby(models.Model):
    title = models.CharField(verbose_name='Vestibiulis', max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, created at {self.created}'
