from django.shortcuts import render, redirect

from iron_recipes.common.forms import CommentForm
from iron_recipes.recipes.forms import RecipeAddForm, RecipeDeleteForm, RecipeEditForm
from iron_recipes.recipes.models import Recipe


# Create your views here.

def recipe_add(request):
    form = RecipeAddForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.user = request.user
        recipe.save()
        return redirect('index')

    context = {"form": form}
    return render(request, 'recipes/recipe-add-page.html', context)


def recipe_details(request, recipe_name):
    comment_form = CommentForm()
    recipe = Recipe.objects.filter(slug=recipe_name).first()
    likes = recipe.like_set.all()
    comments = recipe.comment_set.all()
    # is_recipe_liked_by_user = likes.filter(user=request.user)

    context = {
        "recipe": recipe,
        "likes": likes,
        "comments": comments,
        "comment_form": comment_form,
        # "is_recipe_liked_by_user": is_recipe_liked_by_user,
    }

    return render(request, 'recipes/recipe-details-page.html', context)


def recipe_edit(request, recipe_name):
    recipe = Recipe.objects.get(slug=recipe_name)

    if request.method == "GET":
        form = RecipeEditForm(instance=recipe, initial=recipe.__dict__)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe details', recipe_name)
    context = {"form": form}

    return render(request, 'recipes/recipe-edit-page.html', context)


def recipe_delete(request, recipe_name):
    recipe = Recipe.objects.filter(slug=recipe_name).first()
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    form = RecipeDeleteForm(initial=recipe.__dict__)
    context = {"recipe": recipe, "form": form, "recipe_name": recipe_name}
    return render(request, 'recipes/recipe-delete-page.html', context)
