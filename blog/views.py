from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import AuthorForm, CategoryForm, PostForm

def home(request):
    """
    Vista de inicio (Home) que usa el template global home.html
    """
    return render(request, "home.html")


def about(request):
    """
    Vista 'Acerca de mí' que usa el template global about.html
    """
    return render(request, "about.html")



class PostListView(ListView):
    """
    Listado de Posts (Pages) que se usará en /pages/
    """
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    """
    Detalle de un Post (Page)
    """
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Crear un Post – solo usuarios logueados
    """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        messages.success(self.request, "Post creado correctamente.")
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Editar un Post – solo usuarios logueados
    (si querés luego restringimos más: solo staff, etc.)
    """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        messages.success(self.request, "Post actualizado correctamente.")
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Borrar un Post – solo usuarios logueados
    """
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:list")

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Post eliminado.")
        return super().delete(request, *args, **kwargs)


def search_posts(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).select_related("author", "category")
    context = {"query": query, "results": results}
    return render(request, "blog/search.html", context)


@login_required
def create_author(request):
    """
    Ejemplo de vista con decorador @login_required (requisito de consigna)
    """
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado correctamente.")
            return redirect("blog:list")
    else:
        form = AuthorForm()
    return render(request, "blog/author_form.html", {"form": form})


@login_required
def create_category(request):
    """
    Otra vista con @login_required
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada correctamente.")
            return redirect("blog:list")
    else:
        form = CategoryForm()
    return render(request, "blog/category_form.html", {"form": form})
