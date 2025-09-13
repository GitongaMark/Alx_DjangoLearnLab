from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    # Get the specific book securely
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        # Always use cleaned POST data and forms for validation
        title = request.POST.get("title")
        author = request.POST.get("author")

        # Update the book safely using ORM
        book.title = title
        book.author = author
        book.save()
        return redirect("book_list")  # redirect to a safe page

    return render(request, "relationship_app/templates/relationship_app/edit_book.html", {"book": book})
