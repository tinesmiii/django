
from django.urls import path
from .views import top_sellers, main, advertisement, advertisement_post, mini_game


urlpatterns = [
    path('', main, name = "main"),
    path("top-sellers/", top_sellers, name = "top-sellers"),
    path("advertisement/", advertisement, name = "advertisement"),
    path("advertisement-post/", advertisement_post, name = "advertisement-post"),
    path("mini-game/", mini_game, name = "mini-game")
]
