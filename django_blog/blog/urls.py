from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView 

urlpatterns = [
    # authentication paths
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
  
    # blog post paths
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # comment paths
    path("post/<int:pk>/comment/", views.add_comment, name="add-comment"),
    path("comment/<int:pk>/edit/", views.edit_comment, name="edit-comment"),
    path("comment/<int:pk>/delete/", views.delete_comment, name="delete-comment"),

    # search and tag paths
    path("search/", views.search_posts, name="search"),
    path("tag/<slug:tag_slug>/", views.posts_by_tag, name="posts-by-tag"),
]