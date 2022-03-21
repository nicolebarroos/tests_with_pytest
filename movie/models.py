from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    pass


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    creation_date = models.DateTimeField(default=now, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"
