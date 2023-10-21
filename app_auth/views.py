from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_viev(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse("profile"))
        else:
            return render(request, "app_auth/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect(reverse("profile"))
        else:
            return render(request, "app_auth/login.html", context = {"error" : "Пользователь не найден"})
@login_required(login_url=reverse_lazy("login"))
def profile_viev(request):
    return render(request, "app_auth/profile.html")

def register_viev(request):
    return render(request, "app_auth/register.html")

def logout_viev(request):
    logout(request)
    return redirect(reverse("login"))

# импортируем класс формы
from .forms import RegisterForm
def register(request):
    # если пришел пост запрос (не гет)
    if request.method == "POST":
        # в форму закидываем отправленные данные
        form = RegisterForm(request.POST)
        # проверяем на валидность
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("profile"))
    else:
        form = RegisterForm()
    return render(request, "app_auth/register.html", context = {"form": form})