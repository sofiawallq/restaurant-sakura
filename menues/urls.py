from django.urls import path
from . import views

urlpatterns = [
    path('menues/', views.menues_view, name='menues'),
]    