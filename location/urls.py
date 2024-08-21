from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.locate_restaurant, name='location'),
]