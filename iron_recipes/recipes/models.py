from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField()
    author = models.CharField()  #do fix
    # difficulty = models.Choices()  #do fix
    time_to_cook = models.IntegerField()
    ingredients = models.TextField(max_length=1000)  #do fix
    nutrition = models.TextField(max_length=1000)  #do fix
    description = models.TextField(max_length=200, validators=(), blank=True, null=True)
    how_to_cook = models.TextField()
    number_of_portions = models.IntegerField()
    date_of_publication = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
