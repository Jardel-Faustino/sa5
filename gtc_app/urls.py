from django.urls import path
from gtc_app.views import principal, menu, cadastrar, atualizar, deletar, pesquisar, alfabeto, cadastro
# Cadastra as Urls do nosso Sistema de Cadastro GTC.

urlpatterns = [
    path('', principal, name= 'principal'),
    path('menu/', menu, name= 'menu'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('atualizar/', atualizar, name='atualizar'),
    path('deletar/', deletar, name='deletar'),
    path('pesquisar/', pesquisar, name='pesquisar'),
    path('alfabeto/', alfabeto, name='alfabeto'),
    path('cadastro/', cadastro, name = 'cadastro')
]
