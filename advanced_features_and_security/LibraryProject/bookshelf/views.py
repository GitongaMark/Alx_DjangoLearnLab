from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

def book_list(request):
    books = Book.objects.all()  # ✅ ORM query — parameterized, safe
    return render(request, 'bookshelf/book_list.html', {'books': books})

def form_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Do something with cleaned_data (e.g., save to DB or print)
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            year = form.cleaned_data['publication_year']
            print(f"Added: {title} by {author} ({year})")
            # In real app, you'd save to database here
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

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
