from django.contrib import admin

from iron_recipes.recipes.models import Recipe


# Register your models here.

from django.utils.translation import gettext_lazy as _


class MyCustomRecipeFilter(admin.SimpleListFilter):
    title = _('custom filter')
    parameter_name = 'custom_filter'

    def lookups(self, request, model_admin):
        # define the filter options
        return (
            ('option1', _('By Difficulty: Easy')),
            ('option2', _('By Difficulty: Medium')),
            ('option3', _('By Difficulty: Hard')),
            ('option4', _('By Difficulty: Very Hard')),
        )

    def queryset(self, request, queryset):
        # apply the filter to the queryset
        if self.value() == 'option1':
            return queryset.filter(difficulty='Easy')
        if self.value() == 'option2':
            return queryset.filter(difficulty='Medium')
        if self.value() == 'option3':
            return queryset.filter(difficulty='Hard')
        if self.value() == 'option4':
            return queryset.filter(difficulty='Very Hard')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_publication', 'time_to_cook',)
    list_filter = [MyCustomRecipeFilter]
    search_fields = ['name']

