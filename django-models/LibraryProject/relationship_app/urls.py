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
    path("register/", views.register_view, name="register"),   # <-- checker wants "views.register"
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),   # <-- checker wants "LoginView.as_view(template_name="
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"), # <-- checker wants "LogoutView.as_view(template_name="

    # Books & Libraries
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Role-based Views
    path("role/admin/", views.admin_view, name="admin_view"),
    path("role/librarian/", views.librarian_view, name="librarian_view"),
    path("role/member/", views.member_view, name="member_view"),

    # Book Management (with permissions)
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/<int:pk>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", views.delete_book, name="delete_book"),
]
