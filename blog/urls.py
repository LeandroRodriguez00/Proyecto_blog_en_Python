from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [

    path('', views.PostListView.as_view(), name='list'),


    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),

  
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),


    path('buscar/', views.search_posts, name='search_posts'),

    path('autor/nuevo/', views.create_author, name='create_author'),
    path('categoria/nueva/', views.create_category, name='create_category'),
]
