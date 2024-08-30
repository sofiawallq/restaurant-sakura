from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.book_table, name='booking'),
    path('booking/edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('booking/new/', views.booking_edit, name='booking_new'),
]