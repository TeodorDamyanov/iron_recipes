from django.db import models

from iron_recipes.accounts.models import IronRecipeUser
from iron_recipes.recipes.models import Recipe


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_time_of_publication',)


class Like(models.Model):
    to_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(to=IronRecipeUser, on_delete=models.CASCADE, default=1)
