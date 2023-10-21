
from django.urls import path
from .views import login_viev, profile_viev, register_viev, logout_viev


urlpatterns = [
    path("login/", login_viev, name = "login"),
    path("profile/", profile_viev, name = "profile"),
    path("register/", register_viev, name = "register"),
    path("exit/", logout_viev, name = "logout")
]
