from django.urls import path
from . import views

urlpatterns = [
    path('', views.locate_restaurant, name='location'),
]