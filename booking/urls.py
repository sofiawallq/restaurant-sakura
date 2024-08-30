from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_table, name='book_table'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('booking/new/', views.booking_edit, name='booking_new'),
]