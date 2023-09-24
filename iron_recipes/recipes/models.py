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
    name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='images')
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, default='difficulty')
    time_to_cook = models.IntegerField()
    ingredients = models.TextField(max_length=80)
    nutrition = models.TextField(max_length=80)
    description = models.TextField(max_length=80, blank=True, null=True)
    cooking_method = models.TextField(max_length=80)
    number_of_portions = models.IntegerField()
    date_of_publication = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    user = models.ForeignKey(to=IronRecipeUser, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}--{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
