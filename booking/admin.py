from django.contrib import admin
from .models import BookATable
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(BookATable)
class BookATableAdmin(admin.ModelAdmin):

    list_display = ('firstname', 'lastname', 'date', 'time', 'guests', 'message', 'read',)
    list_filter = ('date', 'time', 'read')
    search_fields = ('firstname', 'lastname', 'email')
    ordering = ('-date', '-time')

    # Customize the form for adding/editing entries
    fields = ('firstname', 'lastname', 'email', 'date', 'time', 'guests', 'message', 'read')