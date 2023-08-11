from django.urls import path
from .views import *


urlpatterns = [
    path('add/', recipe_add, name="recipe add"),
    path('details/<slug:recipe_name>/', recipe_details, name="recipe details"),
    path('edit/<slug:recipe_name>/', recipe_edit, name="recipe edit"),
    path('delete/<slug:recipe_name>/', recipe_delete, name="recipe delete"),
]
