from django.db import models
from ckeditor.fields import RichTextField  


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
 
    title = models.CharField("Título", max_length=120)
    subtitle = models.CharField("Subtítulo", max_length=200, blank=True)
    content = RichTextField("Contenido")

    image = models.ImageField("Imagen", upload_to="posts/", blank=True, null=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Autor",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name="Categoría",
    )

    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
