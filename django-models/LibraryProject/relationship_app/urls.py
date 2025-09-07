from django.urls import path
from .views import list_books
from django.shortcuts import redirect
from .views import (
    register_view, CustomLoginView, CustomLogoutView,
    list_books, LibraryDetailView,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)

# Namespace for this app (helps avoid clashes later)
app_name = "relationship_app"

# Simple homepage redirect (redirects "/" to books list)
def home(request):
    return redirect("relationship_app:list_books")

urlpatterns = [
    # Homepage
    path("", home, name="home"),

    # Authentication
    path("register/", register_view, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),

    # General Views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Role-based Views
    path("role/admin/", admin_view, name="admin_view"),
    path("role/librarian/", librarian_view, name="librarian_view"),
    path("role/member/", member_view, name="member_view"),

    # Book Management (with custom permissions)
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:pk>/", edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", delete_book, name="delete_book"),
]
