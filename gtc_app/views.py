from django.shortcuts import render, redirect  
from .forms import usuarioform  
from .models import usuario, pais

# Criar as Visualizações das Rotas do nosso Sistema de Cadastro GTC.
def menu (request):
    return render(request, "gtc_app/rotas/menu.html")

def principal (request):
    # Busca os 10 últimos usuários cadastrados
    ultimos_usuarios = usuario.objects.order_by('-id')[:10]
    # Realiza uma consulta ao banco de dados para buscar os 10 últimos registros da tabela Usuario.
    # O método order_by('-id') ordena os registros em ordem decrescente com base no campo id.
    # O slicing [:10] retorna apenas os 10 primeiros registros após a ordenação.

    return render(request, "gtc_app/global/principal.html", {'pagina_ativa': 'principal', 'ultimos_usuarios': ultimos_usuarios})
    # Retorna uma resposta HTTP renderizando o template 'sua_template.html'
    # e passando os últimos usuários encontrados na consulta como contexto para o template,
    # sob o nome 'ultimos_usuarios'. Isso permite que os dados sejam acessados e exibidos no template.

def cadastrar (request):
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST (ou seja, o formulário foi submetido)
        form = usuarioform(request.POST)  # Cria uma instância do formulário UsuarioForm com os dados submetidos
        if form.is_valid():  # Verifica se os dados do formulário são válidos
            form.save()  # Salva os dados do formulário no banco de dados
            return redirect('sucesso')  # Redireciona para a página de sucesso após o envio do formulário
    else:  # Se a requisição não for do tipo POST
        form = usuarioform()  # Cria uma nova instância do formulário UsuarioForm (vazio)
    paises = pais.objects.all()  # Recupere todos os registros da tabela Paises
    return render(request, 'gtc_app/rotas/cadastrar.html', {'form': form, 'paises': paises})  # Renderiza o template 'cadastrar.html' com o formulário e passando 'paises' para o contexto do template

def atualizar (request):
    return render(request, "gtc_app/rotas/atualizar.html", {'pagina_ativa': 'atualizar'})

def deletar (request):
    return render(request, "gtc_app/rotas/deletar.html", {'pagina_ativa': 'deletar'})

def pesquisar (request):
    return render(request, "gtc_app/rotas/pesquisar.html", {'pagina_ativa': 'pesquisar'})

def sucesso(request):
    return render(request, 'sucesso.html')
