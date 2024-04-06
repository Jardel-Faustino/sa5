from django.shortcuts import render

# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.

def index (request):
    return render(request, "gtc_app/global/index.html",)

def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    return render(request, "gtc_app/rotas/principal.html", {'pagina_ativa': 'principal'})

def cadastrar (request):
    return render(request, "gtc_app/rotas/cadastrar.html", {'pagina_ativa': 'cadastrar'})

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar'})

def deletar (request):
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar'})

def pesquisar (request):
    return render(request, "gtc_app/rotas/pesquisar.html", {'pagina_ativa': 'pesquisar'})