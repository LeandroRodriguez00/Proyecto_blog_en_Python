from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/nuevo/', views.create_author, name='create_author'),
    path('categoria/nueva/', views.create_category, name='create_category'),
    path('post/nuevo/', views.create_post, name='create_post'),
    path('buscar/', views.search_posts, name='search_posts'),
]
