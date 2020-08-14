from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80, default='Author Name')
    bio = models.TextField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=50, default='Recipe')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(default='')
    time_required = models.CharField(max_length=24, default='')
    instructions = models.TextField(default='')

    def __str__(self):
        return f"{self.title} - {self.author.name}"
