from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.book_table, name='booking'),
]