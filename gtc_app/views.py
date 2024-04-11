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

from django.shortcuts import render
from .models import usuario, pais  # Importe os modelos que você está usando para o cadastro

def cadastrar(request):

    mensagem_sucesso = None
    mensagem_erro = None
    email_erro = None

    if request.method == 'POST':
        nome = request.POST.get("nome").capitalize()  # Garante que a primeira letra do nome seja maiúscula
        data_nascimento = request.POST.get("data_nascimento")
        email = request.POST.get("email")
        nome_pais = request.POST.get("pais")  # Obtém o nome do país do formulário
        
        if usuario.objects.filter(email=email).exists():
            paises = pais.objects.all() 
            email_erro = "Este 'E-MAIL' já está em uso. Por favor, escolha outro e-mail."
            mensagem_erro = "Falha no Cadastramento!!!"
        else:
            try:
                pais_obj = pais.objects.get(nome=nome_pais)
                novo_usuario = usuario(nome=nome, data_nascimento=data_nascimento, email=email, pais=pais_obj)
                novo_usuario.save()
                mensagem_sucesso = "Cadastro Realizado com Sucesso!!!"
            except Exception as e:
                mensagem_erro = f"Falha no Cadastramento: {str(e)}"

    paises = pais.objects.all() 
    return render(request, 'gtc_app/rotas/cadastrar.html', {'pagina_ativa': 'cadastrar', 'paises': paises, 'mensagem_erro': mensagem_erro, "email_erro":email_erro, "mensagem_sucesso":mensagem_sucesso})


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

    h3 = ""  # Inicialize a variável
    if not nome_pesquisado and not letra_selecionada:  # Se tanto o campo de pesquisa quanto a letra selecionada estiverem vazios
        h3 = "Lista de Usuários"
        pesquisando["resultado"] = usuario.objects.all()  # Obtém todos os usuários

    elif letra_selecionada:  # Se uma letra foi selecionada
        h3 = f"Lista de Usuários com a Letra '{request.GET.get('letra', "").upper()}'"# Converte para maiúsculas
        pesquisando["resultado"] = usuario.objects.filter(nome__istartswith=letra_selecionada)
        
    else:  # Se um nome foi pesquisado
        h3 = f"Resultado da Pesquisa: '{nome_pesquisado}'"
        pesquisando["resultado"] = usuario.objects.filter(nome__iexact=nome_pesquisado)
         
    return render(request, "gtc_app/rotas/pesquisar.html", {'pagina_ativa': 'pesquisar', 'pesquisando': pesquisando, 'h3':h3})

def alfabeto(request):
    return render(request, "gtc_app/rotas/alfabeto.html")

