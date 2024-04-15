from django.shortcuts import render, get_object_or_404
from .models import usuario, pais
from django.http import HttpResponseBadRequest
from django.urls import reverse
from datetime import datetime

# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.
def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    global data_formatada

    # Obtendo os usuários ordenados por ID
    usuarios = usuario.objects.all().order_by('-id')[:10]
    
    # Mapeamento dos meses em português
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    # Formatando a data de criação de cada usuário
    for user in usuarios:
        data_formatada = "{}/{}/{}".format(
            user.data_nascimento.day,
            meses[user.data_nascimento.month],
            user.data_nascimento.year
        )

    # Armazenar data_formatada na sessão do usuário
    request.session['data_formatada'] = data_formatada

    return render(request, "gtc_app/global/principal.html", {'pagina_ativa': 'principal', 'usuarios': usuarios, "data_formatada":data_formatada})

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

def atualizar(request):
    pesquisando = {}
    data_formatada = request.session.get('data_formatada', None)

    nome_pesquisado = request.POST.get("nome_pes") if request.method == 'POST' else request.GET.get("nome", "")
    letra_selecionada = request.GET.get("letra", "").lower()

    h3 = ""
    if not nome_pesquisado and not letra_selecionada:
        h3 = "Lista de Usuários"
        pesquisando["resultado"] = usuario.objects.all()

    elif letra_selecionada:
        h3 = f"Lista de Usuários com a Letra '{letra_selecionada.upper()}'"
        pesquisando["resultado"] = usuario.objects.filter(nome__istartswith=letra_selecionada)
        
    else:
        h3 = f"Resultado da Pesquisa: '{nome_pesquisado}'"
        pesquisando["resultado"] = usuario.objects.filter(nome__iexact=nome_pesquisado)
    
    if request.method == 'POST':
        user_id = request.POST.get("id")
        if user_id:
            try:
                user = usuario.objects.get(id=user_id)
                user.nome = request.POST.get("nome")
                user.data_nascimento = request.POST.get("data_nascimento")
                user.email = request.POST.get("email")
                
                # Buscando o objeto país correspondente ao nome enviado no formulário
                nome_pais = request.POST.get("pais")
                if nome_pais:
                    pais_obj = pais.objects.get(nome=nome_pais)
                    user.pais = pais_obj
                
                user.save()
                
                # Se a atualização for bem-sucedida, redirecione para a página de atualização
                usuarios = usuario.objects.all()
                paises = pais.objects.all() 
                return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar', 'usuarios': usuarios, 'pesquisando': pesquisando, 'h3': h3, "data_formatada": data_formatada, "paises":paises})
            except usuario.DoesNotExist:
                return HttpResponseBadRequest("Usuário não encontrado")
    
    # Restante do código permanece o mesmo
    usuarios = usuario.objects.all()
    paises = pais.objects.all() 
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar', 'usuarios': usuarios, 'pesquisando': pesquisando, 'h3': h3, "data_formatada": data_formatada, "paises":paises})

def deletar(request):
    pesquisando = {}
    data_formatada = request.session.get('data_formatada', None)
    
    nome_pesquisado = request.POST.get("nome") if request.method == 'POST' else request.GET.get("nome", "")
    letra_selecionada = request.GET.get("letra", "").lower()  # Obtém a letra selecionada, convertendo para minúsculo

    h3 = ""  # Inicialize a variável
    if not nome_pesquisado and not letra_selecionada:  # Se tanto o campo de pesquisa quanto a letra selecionada estiverem vazios
        h3 = "Lista de Usuários"
        pesquisando["resultado"] = usuario.objects.all()  # Obtém todos os usuários

    elif letra_selecionada:  # Se uma letra foi selecionada
        h3 = f"Lista de Usuários com a Letra '{request.GET.get('letra', '').upper()}'"  # Converte para maiúsculas
        pesquisando["resultado"] = usuario.objects.filter(nome__istartswith=letra_selecionada)
        
    else:  # Se um nome foi pesquisado
        h3 = f"Resultado da Pesquisa: '{nome_pesquisado}'"
        pesquisando["resultado"] = usuario.objects.filter(nome__iexact=nome_pesquisado)
        
    if request.method == 'POST':
        id_usuario = request.POST.get("id")
        if id_usuario:
            try:
                delete = usuario.objects.get(id=id_usuario)
                delete.delete()
            except usuario.DoesNotExist:
                return HttpResponseBadRequest("Usuário não encontrado")

    usuarios = usuario.objects.all() 
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar', 'usuarios': usuarios, 'pesquisando': pesquisando, 'h3': h3, "data_formatada":data_formatada})


def pesquisar(request):
    pesquisando = {}
    data_formatada = request.session.get('data_formatada', None)
    
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
         
    return render(request, "gtc_app/rotas/pesquisar.html", {'pagina_ativa': 'pesquisar', 'pesquisando': pesquisando, 'h3':h3, "data_formatada":data_formatada})

def alfabeto(request):
    return render(request, "gtc_app/rotas/alfabeto.html")
