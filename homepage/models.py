from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=80, default='Author Name')
    bio = models.TextField(default='')
    
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    title = models.CharField(max_length=50, default='Recipe')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(default='')
    time_required = models.CharField(max_length=24, default='')
    instructions = models.TextField(default='')

    def __str__(self):
        return f"{self.title} - {self.author.name}"
    