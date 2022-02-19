from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Account(models.Model):

    user = models.OneToOneField(
        User,
        null=False,
        on_delete=models.CASCADE,
    )

    favourite_movies = models.ManyToManyField(
        Movie,
    )

    def __str__(self) -> str:
        return f"{self.user.username} | {self.user.email} | {self.favourite_movies}"
