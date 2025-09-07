from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, permission_required

from .models import Book, Author, Library


# ------------------------
# General Views
# ------------------------

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ------------------------
# Authentication Views
# ------------------------

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect("relationship_app:list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


# ------------------------
# Role-Based Access Views
# ------------------------

def is_admin(user):
    return user.is_authenticated and user.profile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and user.profile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and user.profile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# ------------------------
# Book Management (Custom Permissions)
# ------------------------

@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    authors = Author.objects.all()

    if not authors.exists():
        return render(request, "relationship_app/add_book.html", {
            "authors": authors,
            "error": "No authors available. Please add an author first."
        })

    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        year = request.POST.get("publication_year")

        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect("relationship_app:list_books")

    return render(request, "relationship_app/add_book.html", {"authors": authors})


@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.publication_year = request.POST.get("publication_year")
        author_id = request.POST.get("author")
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect("relationship_app:list_books")

    authors = Author.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": authors})


@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("relationship_app:list_books")

    return render(request, "relationship_app/delete_book.html", {"book": book})
