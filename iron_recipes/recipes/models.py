from django.db import models
from django.template.defaultfilters import slugify

from iron_recipes.accounts.models import IronRecipeUser


# Create your models here.

DIFFICULTY_CHOICES = (
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
    ("Very Hard", "Very Hard"),
)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, default='difficulty')
    time_to_cook = models.IntegerField()
    ingredients = models.TextField(max_length=1000)
    nutrition = models.TextField(max_length=1000)
    description = models.TextField(max_length=200, validators=(), blank=True, null=True)
    cooking_method = models.TextField()
    number_of_portions = models.IntegerField()
    date_of_publication = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    user = models.ForeignKey(to=IronRecipeUser, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}--{self.id}")
        return super().save(*args, **kwargs)
