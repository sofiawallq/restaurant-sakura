from django.urls import path
from . import views

urlpatterns = [
    path('menues/', views.menues_view, name='menues'),
    path('food-menu/', food_menu_view, name='food_menu'),
]    