from django.shortcuts import render
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
            return render(request, 'gtc_app/rotas/cadastrar.html', {'pagina_ativa': 'cadastrar', 'paises': paises})  # Redireciona para a mesma página sem parâmetros de cadastro

    paises = pais.objects.all() 
    return render(request, 'gtc_app/rotas/cadastrar.html', {'pagina_ativa': 'cadastrar', 'paises': paises})

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar'})

def deletar (request,id=0):
    delete = usuario.objects.get(id=id)
    delete.delete()
    usuarios = usuario.objects.all() 
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar', 'usuarios': usuarios})

def pesquisar(request):
    pesquisando = {}
    
    nome_pesquisado = request.POST.get("nome") if request.method == 'POST' else request.GET.get("nome", "")
    letra_selecionada = request.GET.get("letra", "").lower()  # Obtém a letra selecionada, convertendo para minúsculo
    
    if not nome_pesquisado and not letra_selecionada:  # Se tanto o campo de pesquisa quanto a letra selecionada estiverem vazios
        pesquisando["resultado"] = usuario.objects.all()  # Obtém todos os usuários
    elif letra_selecionada:  # Se uma letra foi selecionada
        pesquisando["resultado"] = usuario.objects.filter(nome__istartswith=letra_selecionada)
    else:  # Se um nome foi pesquisado
        pesquisando["resultado"] = usuario.objects.filter(nome__iexact=nome_pesquisado)
         
    return render(request, "gtc_app/rotas/pesquisar.html", {'pagina_ativa': 'pesquisar', 'pesquisando': pesquisando})

def sucesso(request):
    return render(request, "gtc_app/rotas/sucesso.html")

def alfabeto(request):
    return render(request, "gtc_app/rotas/alfabeto.html")

