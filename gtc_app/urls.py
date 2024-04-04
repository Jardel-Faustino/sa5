from django.urls import path
from gtc_app.views import index, menu, principal, cadastrar, atualizar, deletar, pesquisar

# Cadastra as Urls do nosso Sistema de Cadastro GTC.

urlpatterns = [
    path('', index),
    path('menu', menu, name= 'menu'),
    path('principal', principal, name= 'principal'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('atualizar', atualizar, name='atualizar'),
    path('deletar', deletar, name='deletar'),
    path('pesquisar', pesquisar, name='pesquisar'),
]
