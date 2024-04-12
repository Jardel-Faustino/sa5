from django.shortcuts import render, get_object_or_404
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
         
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar', 'pesquisando': pesquisando, 'h3':h3})

def deletar(request):
    pesquisando = {}
    
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
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar', 'usuarios': usuarios, 'pesquisando': pesquisando, 'h3': h3})


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

def cadastro(request):
    user_id = request.GET.get("id")
    
    # Inicializar variáveis
    user = None
    data_nascimento_str = None
    
    # Se o ID do usuário foi fornecido, busque o usuário
    if user_id:
        user = get_object_or_404(usuario, id=user_id)
        # Certifique-se de que o usuário tenha data de nascimento antes de tentar formatá-la
        if user.data_nascimento:
            data_nascimento_str = user.data_nascimento.strftime('%Y/%d/%m')
    
    mensagem_sucesso = None
    mensagem_erro = None

    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.POST.get("nome", "").capitalize()  # Garante que a primeira letra do nome seja maiúscula
        data_nascimento = request.POST.get("data_nascimento", "")
        email = request.POST.get("email", "")
        nome_pais = request.POST.get("pais", "")

        # Verifique se outro usuário já está usando o mesmo e-mail (exceto o próprio usuário atual)
        if usuario.objects.filter(email=email).exclude(id=user_id).exists():
            mensagem_erro = "Este 'E-MAIL' já está em uso por outro usuário. Por favor, escolha outro e-mail."
        else:
            try:
                # Tentar obter o país com base no nome
                pais_obj = pais.objects.get(nome=nome_pais)

                # Converter `data_nascimento` para objeto datetime
                try:
                    data_nascimento = datetime.strptime(data_nascimento, '%Y/%d/%m')
                except ValueError:
                    raise ValidationErro("Data de nascimento inválida. Por favor, use o formato DD/MM/YYYY.")
                
                # Atualizar as informações do usuário
                user.nome = nome
                user.data_nascimento = data_nascimento
                user.email = email
                user.pais = pais_obj
                user.save()

                mensagem_sucesso = "Dados atualizados com sucesso!"
            except Exception as e:
                mensagem_erro = f"Falha na atualização: {str(e)}"

    # Obtenha a lista de países para usar no template
    paises = pais.objects.all()

    # Renderize a página com os dados do usuário e outros dados necessários
    return render(request, 'gtc_app/rotas/cadastro.html', {'pagina_ativa': 'atualizar', 'user': user, 'paises': paises, 'mensagem_erro': mensagem_erro, 'mensagem_sucesso': mensagem_sucesso, 'data_nascimento_str': data_nascimento_str})