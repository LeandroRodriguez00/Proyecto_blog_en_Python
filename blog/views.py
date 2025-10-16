from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Post
from .forms import AuthorForm, CategoryForm, PostForm

def home(request):
    posts = Post.objects.select_related("author", "category").all()
    return render(request, "blog/post_list.html", {"posts": posts})

def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado correctamente.")
            return redirect("blog:home")
    else:
        form = AuthorForm()
    return render(request, "blog/author_form.html", {"form": form})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada correctamente.")
            return redirect("blog:home")
    else:
        form = CategoryForm()
    return render(request, "blog/category_form.html", {"form": form})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post creado correctamente.")
            return redirect("blog:home")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

def search_posts(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).select_related("author", "category")
    context = {"query": query, "results": results}
    return render(request, "blog/search.html", context)
