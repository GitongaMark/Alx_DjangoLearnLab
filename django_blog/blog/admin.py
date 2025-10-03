from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Comment
from taggit.models import Tag  # only if using taggit

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)
    prepopulated_fields = {}  # your choices

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content',)
