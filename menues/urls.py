from django.urls import path
from .views import menues_view

urlpatterns = [
    path('', menues_view, name='menues'),
]