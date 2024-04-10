from django.shortcuts import render, redirect
from .models import usuario, pais
from django.http import HttpResponseBadRequest
dados = []

# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.
def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    usuarios = usuario.objects.all() 
    return render(request, "gtc_app/global/principal.html", {'pagina_ativa': 'principal', 'usuarios': usuarios})

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        data_nascimento = request.POST.get("data_nascimento")
        email = request.POST.get("email")
        nome_pais = request.POST.get("pais")  # Obtém o nome do país do formulário

        # Verifica se o e-mail já está em uso
        if usuario.objects.filter(email=email).exists():
            paises = pais.objects.all() 
            mensagem_erro = "Este e-mail já está em uso. Por favor, escolha outro e-mail."
            return render(request, "gtc_app/rotas/cadastrar.html", {'pagina_ativa': 'cadastrar', 'paises': paises, "mensagem_erro": mensagem_erro})
        else:
            # Obtenha o objeto Pais correspondente ao nome selecionado
            pais_obj = pais.objects.get(nome=nome_pais)
            # Crie uma instância do modelo e salve os dados no banco de dados
            novo_usuario = usuario(nome=nome, data_nascimento=data_nascimento, email=email, pais=pais_obj)
            novo_usuario.save()
            paises = pais.objects.all() 
            return render(request, 'gtc_app/rotas/cadastrar.html', {'pagina_ativa': 'cadastrar', 'paises': paises})

    paises = pais.objects.all() 
    return render(request, 'gtc_app/rotas/cadastrar.html', {'pagina_ativa': 'cadastrar', 'paises': paises})

'''def salvos(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        nome_us = request.POST.get("nome")
        data_nascimento_us = request.POST.get("data_nascimento")
        email_us = request.POST.get("email")
        pais_us = request.POST.get("pais")  # Obter o nome do país

        # Verifica se o e-mail já está em uso
        

        # Obter a instância do país correspondente ao nome fornecido
        pais_instancia = pais.objects.get(nome=pais_us)

        # Cria um novo objeto usuario com todos os campos preenchidos
        novo_usuario = usuario.objects.create(nome=nome_us, data_nascimento=data_nascimento_us, email=email_us, pais=pais_instancia)
        
        return render(request, "gtc_app/global/principal.html", {'pagina_ativa': 'principal',"usuarios": usuarios})'''

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar'})

def deletar (request):
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar'})

def pesquisar (request):
    if request.POST:
        pessoa = request.POS.get("nome_pesquisado")
        usuario.objects.filter(nome__icontains=pessoa)
    usuarios ={
        "nome_pesquisadonome" : usuarios
    }
    return render(request, "gtc_app/rotas/pesquisar.html",  {'usuarios': usuarios, 'pagina_ativa': 'pesquisar'})

def sucesso(request):
    return render(request, 'sucesso.html')



