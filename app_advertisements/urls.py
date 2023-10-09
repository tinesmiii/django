
from django.urls import path
from .views import top_sellers, main, login, profile, register, advertisement, advertisement_post, mini_game


urlpatterns = [
    path('', main, name = "main"),
    path("top-sellers/", top_sellers, name = "top-sellers"),
    path("login/", login, name = "login"),
    path("profile/", profile, name = "profile"),
    path("register/", register, name = "register"),
    path("advertisement/", advertisement, name = "advertisement"),
    path("advertisement-post/", advertisement_post, name = "advertisement-post"),
    path("mini-game/", mini_game, name = "mini-game")
]
