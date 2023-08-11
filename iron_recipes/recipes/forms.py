from django import forms

from iron_recipes.recipes.models import Recipe


# Create your forms here.


class BaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'photo', 'time_to_cook', 'difficulty', 'ingredients', 'nutrition', 'cooking_method', 'number_of_portions']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Recipe name',
                }
            ),
            # 'photo': forms.ImageField(
            #     attrs={
            #         'placeholder': 'Link to photo',
            #     }
            # ),
            'time_to_cook': forms.NumberInput(
                attrs={
                    'placeholder': 'Cooking time',
                }
            ),
            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'Ingredients',
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition',
                }
            ),
            'cooking_method': forms.Textarea(
                attrs={
                    'placeholder': 'Cooking method',
                }
            ),
            'number_of_portions': forms.NumberInput(
                attrs={
                    'placeholder': 'Number of portions',
                }
            ),
        }
        labels = {
            'name': 'Recipe name',
            'photo': 'Photo',
            'ingredients': 'Ingredients',
            'nutrition': 'Nutrition',
            'cooking_method': 'Method of cooking',
            'number_of_portions': 'Number of portions',
            'difficulty': 'Difficulty',
        }


class RecipeAddForm(BaseForm):
    pass


class RecipeEditForm(BaseForm):
    class Meta:
        model = Recipe
        fields = ['name', 'photo', 'description', 'time_to_cook', 'ingredients', 'nutrition', 'cooking_method', 'number_of_portions']


class RecipeDeleteForm(BaseForm):
    class Meta:
        model = Recipe
        fields = ['name', 'time_to_cook', 'ingredients', 'nutrition', 'cooking_method', 'number_of_portions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance