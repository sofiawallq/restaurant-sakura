from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_table, name='booking'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('booking/booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('booking/delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),
]