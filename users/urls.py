from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html'
        ),
        name='login'
    ),

    path('logout/', views.user_logout, name='logout'),


    path('signup/', views.signup, name='signup'),


    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),


    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url='/accounts/password_change_done/'
        ),
        name='password_change'
    ),

    path(
        'password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done'
    ),
]
