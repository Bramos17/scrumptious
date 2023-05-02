from django.urls import path
from recipes.views import recipe_list, show_recipe, create_recipe, edit_recipe


urlpatterns = [
    path("mine/", recipe_list, name="my_recipe_list"),
    path("recipes/", recipe_list, name="recipe_list"),
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/<int:id>/edit/", edit_recipe, name="edit_recipe"),
]
