from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='landing_page'),
    path('menues/', views.menues_view, name='menues'),
    path('location', views.locate_restaurant, name='location'),
]