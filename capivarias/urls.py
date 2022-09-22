from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('informativo/', views.informativo, name='informativo'),
    path('engracado/', views.engracado, name='engracado'),
    path('fofo/', views.fofo, name='fofo'),
    path('<int:id_capivaria>', views.conteudo, name='conteudo'),
]