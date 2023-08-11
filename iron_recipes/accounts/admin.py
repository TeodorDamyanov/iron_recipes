from django.contrib import admin

from iron_recipes.accounts.models import IronRecipeUser


@admin.register(IronRecipeUser)
class IronRecipeUserAdmin(admin.ModelAdmin):
    pass
