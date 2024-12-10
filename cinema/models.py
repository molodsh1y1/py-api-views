from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        "Actor",
        related_name="movies"
    )
    genres = models.ManyToManyField(
        "Genre",
        related_name="movies"
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name}"
