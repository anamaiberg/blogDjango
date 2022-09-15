from django.shortcuts import render, get_object_or_404
from .models import Capivaria

# Create your views here.


def index(requests):
    capivarias = Capivaria.objects.all()
    return render(requests, 'capivarias/index.html',
                  {'capivarias': capivarias})


def informativo(requests):
    capivarias = Capivaria.objects.filter(categoria="1")
    return render(requests, 'capivarias/index.html',
                  {'capivarias': capivarias})


def engracado(requests):
    capivarias = Capivaria.objects.filter(categoria="2")
    return render(requests, 'capivarias/index.html',
                  {'capivarias': capivarias})


def fofo(requests):
    capivarias = Capivaria.objects.filter(categoria="3")
    return render(requests, 'capivarias/index.html',
                  {'capivarias': capivarias})


def conteudo(requests, id_capivaria):
    capivarias = get_object_or_404(Capivaria, id=id_capivaria)
    return render(requests, 'capivarias/conteudo.html',
                  {'capivarias': capivarias})
