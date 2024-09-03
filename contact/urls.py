from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_restaurant, name='contact'),
]