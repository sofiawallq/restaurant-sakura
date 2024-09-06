from django.contrib import admin
from .models import ContactRestaurant
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(ContactRestaurant)
class ContactRestaurantAdmin(admin.ModelAdmin):

    list_display = ('subject', 'name', 'message', 'read',)