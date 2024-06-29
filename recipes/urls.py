from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('signup/', views.signup, name='signup'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('edit_recipe/<int:pk>/', views.edit_recipe, name='edit_recipe'),
]


   
