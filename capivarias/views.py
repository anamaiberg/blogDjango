from django.shortcuts import render, get_object_or_404
from .models import Capivaria

# Create your views here.


def index(requests):
    capivarias = Capivaria.objects.all()
    return render(requests, 'capivarias/index.html',
                  {'capivarias': capivarias})