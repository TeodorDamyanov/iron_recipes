from django.db import models

# Create your models here.


class Photo(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_image = models.URLField()
    # cooking_difficulty = models.Choices()  #do fix
    description = models.TextField(max_length=200, validators=(), blank=True, null=True)
