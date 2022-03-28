from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    pass


class Actors(models.Model): #new
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    script = models.FileField('Roteiro', upload_to='files/', null=False, blank=False)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    creation_date = models.DateTimeField(default=now, blank=False, null=False)
    actors = models.ManyToManyField(Actors)  #new

    def __str__(self):
        return f"{self.title}"
