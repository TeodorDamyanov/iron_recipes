from django.contrib import admin

from iron_recipes.accounts.models import IronRecipeUser

from django.utils.translation import gettext_lazy as _


class MyCustomUserFilter(admin.SimpleListFilter):
    title = _('custom filter')
    parameter_name = 'custom_filter'

    def lookups(self, request, model_admin):
        # define the filter options
        return (
            ('option1', _('Is employee')),
            ('option2', _('Is staff')),
        )

    def queryset(self, request, queryset):
        # apply the filter to the queryset
        if self.value() == 'option1':
            return queryset.filter(is_employee="True")
        if self.value() == 'option2':
            return queryset.filter(is_staff="True")


@admin.register(IronRecipeUser)
class IronRecipeUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_employee')
    list_filter = [MyCustomUserFilter]
    search_fields = ['username']
