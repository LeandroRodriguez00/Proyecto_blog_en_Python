from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email", "bio"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "subtitle", "content", "image", "author", "category"]
