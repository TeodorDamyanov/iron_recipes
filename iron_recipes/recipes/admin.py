from django.contrib import admin

from iron_recipes.recipes.models import Recipe


# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
