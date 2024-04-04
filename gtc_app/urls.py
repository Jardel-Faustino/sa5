from django.urls import path
from gtc_app.views import index, menu, principal, cadastrar, atualizar, deletar, pesquisar

# Cadastra as Urls do nosso Sistema de Cadastro GTC.

urlpatterns = [
    path('', index),
    path('menu', menu),
    path('principal', principal),
    path('cadastrar', cadastrar),
    path('atualizar', atualizar),
    path('deletar', deletar),
    path('pesquisar', pesquisar),
]
