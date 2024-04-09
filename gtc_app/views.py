from django.shortcuts import render
from .models import usuario, pais
from django.http import HttpResponseBadRequest

usuarios = usuario.objects.all()
paises = pais.objects.all()  # Recupere todos os registros da tabela Paises

# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.
def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    return render(request, "gtc_app/global/principal.html", {'pagina_ativa': 'principal', 'usuario': usuarios})

def cadastrar (request):
    
    return render(request, 'gtc_app/rotas/cadastrar.html', {'paises': paises})  # Renderiza o template 'cadastrar.html' com o formulário e passando 'paises' para o contexto do template

def salvos(request):
    # Captura os dados do formulário
    nome_us = request.POST.get("nome")
    data_nascimento_us = request.POST.get("data_nascimento")
    email_us = request.POST.get("email")
    pais_us = request.POST.get("pais")  # Obter o nome do país
    # Verifica se o e-mail já está em uso
        # Verifica se o e-mail já está em uso
    if usuario.objects.filter(email=email_us).exists():
        mensagem_erro = "Este e-mail já está em uso. Por favor, escolha outro e-mail."
        return render(request, "gtc_app/rotas/cadastrar.html", {'paises': paises, "mensagem_erro": mensagem_erro})
    # Obter a instância do país correspondente ao nome fornecido
    pais_instancia = pais.objects.get(nome=pais_us)
    # Cria um novo objeto usuario com todos os campos preenchidos
    novo_usuario = usuario.objects.create(nome=nome_us, data_nascimento=data_nascimento_us, email=email_us, pais=pais_instancia)
    # Recupera todos os usuários após criar o novo usuário
    return render(request, "gtc_app/global/principal.html", {"usuarios": usuarios})

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar'})

def deletar (request):
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar'})

def pesquisar (request):
    return render(request, "gtc_app/rotas/pesquisar.html", {'pagina_ativa': 'pesquisar'})

def sucesso(request):
    return render(request, 'sucesso.html')



