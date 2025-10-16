from django.contrib import admin
from .models import Author, Category, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    list_filter = ("category", "author")
    search_fields = ("title", "content")
