from django.urls import path
from .views import menues_view, food_menu_view, drink_menu_view

urlpatterns = [
    path('', menues_view, name='menues'),
    path('food-menu/', food_menu_view, name='food_menu'),
    path('drink-menu/', food_menu_view, name='drink_menu'),
]