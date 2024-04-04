from django.shortcuts import render

# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.

def index (request):
    return render(request, "gtc_app/global/index.html")

def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    return render(request, "gtc_app/rotas/principal.html")

def cadastrar (request):
    return render(request, "gtc_app/rotas/cadastrar.html")

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html")

def deletar (request):
    return render(request, "gtc_app/rotas/deletar.html")

def pesquisar (request):
    return render(request, "gtc_app/rotas/pesquisar.html")