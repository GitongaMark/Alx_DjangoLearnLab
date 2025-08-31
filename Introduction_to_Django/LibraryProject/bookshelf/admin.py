from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters (right sidebar)
    list_filter = ("publication_year", "author")

    # Add search bar (searchable by title and author)
    search_fields = ("title", "author")

    # Optional: order by publication year descending
    ordering = ("-publication_year",)
