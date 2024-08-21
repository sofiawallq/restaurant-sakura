from django.contrib import admin
from .models import BookATable
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(BookATable)
class BookATableAdmin(admin.ModelAdmin):

    list_display = ('firstname', 'lastname', 'date', 'time', 'message', 'read',)