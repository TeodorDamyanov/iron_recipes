from django.urls import path, include
from .views import *

from iron_recipes.recipes import views

urlpatterns = [
    path('', index, name="index"),
    path("like/<int:recipe_id>/", like_function, name="like"),
    path("share/<slug:recipe_name>/", share_link, name="share"),
    path("comment/<int:recipe_id>/", add_comment, name="comment"),
]
