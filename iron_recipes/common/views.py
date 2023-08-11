from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from iron_recipes.common.forms import CommentForm, SearchForm
from iron_recipes.common.models import Like
from iron_recipes.recipes.models import Recipe


# Create your views here.


def index(request):
    all_recipes = Recipe.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    user = request.user

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_recipes = all_recipes.filter(name=search_form.cleaned_data['search'])

    context = {
        "all_recipes": all_recipes,
        "comment_form": comment_form,
        "search_form": search_form,
    }
    return render(request, 'common/home-page.html', context)


def like_function(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    liked_object = Like.objects.filter(to_recipe_id=recipe_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_recipe=recipe, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{recipe_id}")


def share_link(request, recipe_name):
    copy(request.META['HTTP_HOST'] + resolve_url('recipe details', recipe_name))

    return redirect(request.META['HTTP_REFERER'] + f"#{recipe_name}")


def add_comment(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_recipe = recipe
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{recipe_id}")
