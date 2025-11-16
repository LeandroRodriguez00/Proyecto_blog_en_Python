from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

from .forms import UserRegisterForm, ProfileForm
from .models import Profile


def signup(request):
    """Registro de usuario nuevo"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente. Ya podés iniciar sesión.")
            return redirect("users:login")
    else:
        form = UserRegisterForm()

    return render(request, "users/signup.html", {"form": form})


@login_required
def profile(request):
    """Vista de perfil con datos extendidos"""
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "users/profile.html", {"profile": profile})


@login_required
def profile_edit(request):
    """Editar datos básicos del usuario + perfil extendido"""
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
  
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.save()

        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("users:profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
    }
    return render(request, "users/profile_edit.html", context)


def user_logout(request):
    """Cerrar sesión y redirigir al home (acepta GET)"""
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("home")
