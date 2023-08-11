from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from iron_recipes.accounts.models import IronRecipeUser


# Create your forms here.


class IronRecipeUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = IronRecipeUser
        fields = ('username', 'email')
        widgets = {'username': forms.TextInput()}


class IronRecipeUserEditForm(forms.ModelForm):
    class Meta():
        model = IronRecipeUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')
        exclude = ('password',)
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'Profile Pic:'
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username"}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password"}))