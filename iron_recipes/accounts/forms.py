from django import forms
from django.contrib.auth.forms import UserCreationForm

from iron_recipes.accounts.models import IronRecipeUser


# Create your forms here.


class IronRecipeUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = IronRecipeUser
        fields = ('username', 'email')
        widgets = {'username': forms.TextInput()}
