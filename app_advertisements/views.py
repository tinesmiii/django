from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    adverts = Advertisement.objects.all()
    context = {"adverts" : adverts}
    return render(request, "app_advertisement/index.html", context=context)

def top_sellers(request):
    return render(request, "app_advertisement/top-sellers.html")

def advertisement(request):
    adverts = Advertisement.objects.all()
    context = {"adverts" : adverts}
    return render(request, "app_advertisement/advertisement.html", context=context)

@login_required(login_url=reverse_lazy("login"))
def advertisement_post(request):
    from .forms import AdvertisementForm
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main")
            return redirect(url)  
              
    form = AdvertisementForm()
    context = {"form":form}
    return render(request, "app_advertisement/advertisement-post.html", context = context)

def mini_game(request):
    import requests
    import json

    url = "https://www.cbr-xml-daily.ru/daily_jsonp.js"

    responce = requests.get(url=url)

    data = responce.text[responce.text.index("{"):responce.text.rindex("}") + 1]

    parsed_data = json.loads(data)

    usd_value = parsed_data["Valute"]["USD"]["Value"]
    
    eur_value = parsed_data["Valute"]["EUR"]["Value"]
    
    context = {"some_info": 123, "usd": usd_value, "eur" : eur_value}
    return render(request, "app_advertisement/mini_game.html", context=context)